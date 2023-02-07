#!/usr/bin/env python3

import asyncio
import drone.connect_drone as cd
import operator
import os
import sys

from mavsdk import System
from pathlib import Path

# Global constants
downloads_path = os.path.join(str(Path.home() / "Downloads"), "FlightLogs")



async def run():
    global downloads_path

    drone = await cd.connect_drone()
    downloads_path = await create_directory(downloads_path)
    
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break
    
    await begin_download(drone)    



async def create_directory(downloads_path):
    if( not os.path.exists(downloads_path)):
        os.mkdir(downloads_path)
    return downloads_path



async def begin_download(drone):
    entries = await get_entries(drone)
    await download_log(drone, entries[0])



async def get_entries(drone):
    entries = await drone.log_files.get_entries()
    entries.sort(key = operator.attrgetter('date'), reverse = True)
    for entry in entries:
        print(f"Log {entry.id} from {entry.date}")
    return entries


async def download_log(drone, entry):
    global downloads_path
    date_without_colon = entry.date.replace(":", "-")
    filename = f"{downloads_path}/log-{date_without_colon}.ulog"
    print(f"Downloading: log {entry.id} from {entry.date} to {filename}")
    previous_progress = -1
    async for progress in drone.log_files.download_log_file(entry, filename):
        new_progress = round(progress.progress*100)
        if new_progress != previous_progress:
            sys.stdout.write(f"\r{new_progress} %")
            sys.stdout.flush()
            previous_progress = new_progress
    print()
    await upload_to_flight_review(filename)



async def upload_to_flight_review(filename):
    flight_review_dir = '/home/nm/developer/FlightReviewApp/flight_review/app'
    os.chdir(flight_review_dir)
    str = 'python3 ./serve.py -f ' + filename

    os.system(str)



if __name__ == "__main__":
    # Run the asyncio loop
    print('fr main program')
    asyncio.run(run())