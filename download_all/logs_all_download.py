#!/usr/bin/env python3

import asyncio
from mavsdk import System
import sys
import drone.connect_drone as connect_drone
from pathlib import Path
import os
import operator


downloads_path = os.path.join(str(Path.home() / "Downloads"), "FlightLogs")



async def run():
    global downloads_path
    drone = await connect_drone.connect_drone()
    downloads_path = await create_directory()
    await begin_download(drone)



async def create_directory():
    if( not os.path.exists(downloads_path)):
        os.mkdir(downloads_path)
    return downloads_path



async def begin_download(drone):
    entries = await get_entries(drone)
    for entry in entries:
        await download_log(drone, entry)



async def get_entries(drone):
    entries = await drone.log_files.get_entries()
    entries.sort(key = operator.attrgetter('date'), reverse = True)
    for entry in entries:
        print(f"Log {entry.id} from {entry.date}")
    return entries



async def download_log(drone, entry):
    date_without_colon = entry.date.replace(":", "-")
    filename = f"{downloads_path}/log-{date_without_colon}.ulog"
    if(not await check_file_exists(filename, entry)):
        print(f"Downloading: log {entry.id} from {entry.date} to {filename}")
        previous_progress = -1
        async for progress in drone.log_files.download_log_file(entry, filename):
            new_progress = round(progress.progress*100)
            if new_progress != previous_progress:
                sys.stdout.write(f"\r{new_progress} %")
                sys.stdout.flush()
                previous_progress = new_progress
    print()



async def check_file_exists(filename, entry):
    #TODO : remove after comparison code is working properly
    print('\nCurrent drone log file : ', entry.date)
    if(not os.path.isfile(filename)):
        print('File does NOT exist : ', filename)
        return False
    else: 
        print("File Exist : ", filename)
        if(os.path.getsize(filename) == entry.size_bytes):
            print('files ARE same size')
            return True
        else: 
            os.remove(filename)
            return False



if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())