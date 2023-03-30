#!/home/nm/dev/FlightLogs/venv python3

'''

'''


import os
import csv
import sys
import glob
import json
# import time
import pytz
import asyncio
import datetime
# import signal
import operator
import subprocess

# import PySimpleGUI as sg
from pathlib import Path
# from mavsdk import System

import layout.layout_vert as lt
from logs import log_paths

# Global constants
_downloads_path_ = os.path.join(str(Path.home() / "Downloads"), "FlightLogs")
_entries_ = {}


async def run(drone):
    # creates download directory and retrieves ulog entries 
    global _downloads_path_, _entries_
    
    await create_directory()
    await get_entries(drone) 


async def create_directory():
    # Creates the directory for downloads if it does not already exist

    global _downloads_path_

    if( not os.path.exists(_downloads_path_)):
        os.mkdir(_downloads_path_)


async def get_entries(drone):
    # Retrieves the ulogs from the drone and sorts them from recent to oldest
    
    global _entries_

    _entries_ = await drone.log_files.get_entries()
    _entries_.sort(key = operator.attrgetter('date'), reverse = True)


async def download_all_logs(drone):
    # Download all ulogs in drone
    
    global _entries_

    for entry in _entries_:
        await download_log(drone, entry)
    

async def entries_to_list():
    # Gets the list of ulogs and creates a list to be displayed in the GUI
    
    global _entries_

    entries_list = []
    for entry in _entries_:
        filename = await rename_file(entry)
        filename = filename + ' ............ ' + str(round(((entry.size_bytes / 1024) / 1000 ),2))+ " MB"
        entries_list.append(filename)
    return entries_list


async def download_log(drone, index):
    # Downloads the selected ulog to the Downloads/FlightLogs/ directory
    
    global _downloads_path_, _entries_

    ulog_path = await log_paths.get_ulogs(drone, index)
    entry = _entries_[index]
    filename = await rename_file(entry)

   # Login information for the PX4, this information may have to change depending on users information. 
    user = 'root'
    password = 'oelinux123'
    ulog_path = '/data/px4/log/'+ulog_path
    ip_address = '192.168.0.113'
    ulog_path_and_name = _downloads_path_ + '/' +filename
    server_ulog = f'{user}@{ip_address}:{ulog_path}'

    if not os.path.isfile(ulog_path_and_name):
        # Download ulog via scp
        sshpass_command = ['sshpass', '-p', password, 'scp', '-r', server_ulog, ulog_path_and_name]
        process = await asyncio.create_subprocess_exec(*sshpass_command)
        await process.wait()

    return ulog_path_and_name


async def rename_file(entry):
    #renames ulog for consistency 

    date_without_colon = entry.date.replace(":", "-")
    filename = f"log-1-{date_without_colon}.ulg"
    filename = filename.replace('T','-')
    filename = filename.replace('Z','')
    return filename


async def create_csv(drone, index):
    # Creates and downloads a csv document that includes the message_to_download data

    filename = await download_log(drone, index)
    message_to_download = '-m vehicle_attitude '
    
    # Change of directory to execute functions that converts the ulog to csv
    change_dir = '/home/nm/dev/FlightLogs/venv/lib/python3.8/site-packages/pyulog/'
    data_csv = message_to_download + filename 
    get_csv = 'python3 ulog2csv.py ' + data_csv
    os.chdir(change_dir)
    os.system(get_csv)


async def create_json(drone, index):
    # Converts and downloads the csv file to a json file.

    global _downloads_path_, _entries_

    # check if file has already been downloaded. 
    filename = await rename_file(_entries_[index])
    filename = filename.replace('.ulg', '')
    while (True): 
        csv_path = await get_csv_path(filename)
        if csv_path == '':
            await create_csv(drone, index)
        else: 
            break

    json_path = csv_path.replace('.csv', '.json')
    data = {}
    with open(csv_path, encoding = 'utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['timestamp']
            data[key] = rows

    with open(json_path, 'w', encoding = 'utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent = 4))


async def get_csv_path(filename):

    csv_path = ''
    matching_files = glob.glob(f"{_downloads_path_}/*{filename}*")
    for file in matching_files:
        if '.csv' in file:
            csv_path = file

    return csv_path


async def upload_to_flight_review(drone, index):
    # Downloads the selected ulog and displays the data in local build of Flight Review.
    # flight_review_directory path to local installation path

    curr_dir = os.getcwd()
    filename = await download_log(drone, index)
    flight_review_dir = '/home/nm/dev/flight_review/app'
    os.chdir(flight_review_dir)
    cmd = ['python3', './serve.py', '-f', filename]
    result = subprocess.Popen(cmd)
    os.chdir(curr_dir)   
    return result


# TODO: Have to find the right spot to put this, so that names have CST
async def zulu_to_cst(zulu_time_str):
    # Converts zulu time zone to central time zone.

    print(f'Zulu time: {zulu_time_str}')
    temp = zulu_time_str.replace('T', ' ')
    temp = temp.replace('Z', '')

    zulu_time_str = temp
    zulu_time = datetime.datetime.strptime(zulu_time_str, "%Y-%m-%d %H:%M:%S")

    # convert the Zulu time to the UTC timezone
    utc_timezone = pytz.timezone('UTC')
    zulu_time = utc_timezone.localize(zulu_time)

    # convert the UTC time to the CST timezone
    cst_timezone = pytz.timezone('US/Central')
    temp = zulu_time.astimezone(cst_timezone)
    cst_time = datetime.datetime.strftime(temp, "%Y-%m-%d %H:%M:%S" )
    print(f'Central time: {cst_time}')
    return cst_time


if __name__ == "__main__":
    # Run the asyncio loop
    print('fr main program')
    asyncio.run(run())