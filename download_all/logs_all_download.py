#!/usr/bin/env python3

import asyncio
from mavsdk import System
import sys
import connect_drone
from pathlib import Path
import os
import filecmp



async def run():
    # drone = System()
    # await drone.connect(system_address="udp://:14550")

    # print("Waiting for drone to connect...")
    # async for state in drone.core.connection_state():
    #     if state.is_connected:
    #         print(f"-- Connected to drone!")
    #         break

    drone = await connect_drone.connect_drone()

    entries = await get_entries(drone)
    for entry in entries:
        await download_log(drone, entry)



async def download_log(drone, entry):
    downloads_path = await check_directory_exists()
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



async def check_directory_exists():
    downloads_path = os.path.join(str(Path.home() / "Downloads"), "FlightLogs")
    if( not os.path.exists(downloads_path)):
        os.mkdir(downloads_path)

    print("Directory created : ", downloads_path)
    return downloads_path



async def check_file_exists(filename, entry):
    print(filename)
    print(entry)
    if(os.path.isfile(filename)):
        print('file size: ', os.path.getsize(filename))
        print('entry size: ', entry.size_bytes)
        if(os.path.getsize(filename) == entry.size_bytes):
            return True
        else: 
            os.remove(filename)
    return False



async def get_entries(drone):
    entries = await drone.log_files.get_entries()
    for entry in entries:
        print(f"Log {entry.id} from {entry.date}")
    return entries



if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())