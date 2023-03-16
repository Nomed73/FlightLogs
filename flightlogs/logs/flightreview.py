#!/home/nm/dev/FlightLogs/venv python3

# usr/bin/env python3
# path/to/myenv/bin/python3


import os
import csv
import sys
import glob
import json
import time
import pytz
import asyncio
import datetime
import operator
import subprocess
from pathlib import Path
from mavsdk import System


# Global constants
_downloads_path_ = os.path.join(str(Path.home() / "Downloads"), "FlightLogs")
_entries_ = {}


async def run(drone):
    global _downloads_path_, _entries_
    
    await create_directory()
    await get_entries(drone) 


async def create_directory():
    global _downloads_path_

    if( not os.path.exists(_downloads_path_)):
        os.mkdir(_downloads_path_)


async def get_entries(drone):
    global _entries_

    _entries_ = await drone.log_files.get_entries()
    _entries_.sort(key = operator.attrgetter('date'), reverse = True)


async def download_all_logs(drone):
    global _entries_

    for entry in _entries_:
        await download_log(drone, entry)
    

async def entries_to_list():
    global _entries_

    entries_list = []
    for entry in _entries_:
        filename = await rename_file(entry)
        filename = filename + ' ............ ' + str(round(((entry.size_bytes / 1024) / 1000 ),2))+ " MB"
        entries_list.append(filename)
    return entries_list


async def download_log(drone, index):
    global _downloads_path_, _entries_

    entry = _entries_[index]
    print("entry size = ", entry.size_bytes)
    print('entry contents = ', entry)
    filename = await rename_file(entry)
    filename = f'{_downloads_path_}/{filename}'
    if not os.path.isfile(filename):
        print(f"Downloading: log {entry.id} from {entry.date} to {filename}")
        previous_progress = -1
        async for progress in drone.log_files.download_log_file(entry, filename):
            new_progress = round(progress.progress*100)
            if new_progress != previous_progress:
                sys.stdout.write(f"\r{new_progress} %")
                sys.stdout.flush()
                previous_progress = new_progress
        print()
    return filename


async def rename_file(entry):
    date_without_colon = entry.date.replace(":", "-")
    filename = f"log-1-{date_without_colon}.ulg"
    filename = filename.replace('T','-')
    filename = filename.replace('Z','')
    return filename


async def create_csv(drone, index):
    filename = await download_log(drone, index)
    message_to_download = '-m vehicle_attitude '
    # directory where the program is to create the csv
    change_dir = '/home/nm/dev/FlightLogs/venv/lib/python3.8/site-packages/pyulog/'
    data_csv = message_to_download + filename 
    get_csv = 'python3 ulog2csv.py ' + data_csv
    
    #TODO: Remove when the program is done. 
    print('filename = ', filename)
 
    os.chdir(change_dir)
    os.system(get_csv)



async def create_json(drone, index):
    global _downloads_path_, _entries_

    # check if file has already been downloaded. 
    filename = await rename_file(_entries_[index])
    print('file to search : ', filename)
    print('directory to search:', _downloads_path_)

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
        # print("File in matching_files : ", file)
        # print('file type is :', type(file))
        if '.csv' in file:
            print('csv file found : ', file)
            csv_path = file
            print('csv_path is : ', csv_path)

    return csv_path


async def upload_to_flight_review(drone, index):

    print("\n\n**** IN FLIGHT REVIEW FUNCTION ****\n\n")
    print("Current Directory : ", os.getcwd())
    curr_dir = os.getcwd()
    filename = await download_log(drone, index)
    print('file name in upload to flight review function : ', filename)
    flight_review_dir = '/home/nm/dev/flight_review/app'
    
    os.chdir(flight_review_dir)
    print("Current Directory : ", os.getcwd())
    cmd = ['python3', './serve.py', '-f', filename]
    result = subprocess.Popen(cmd)
    os.chdir(curr_dir)   
    return result


# TODO: Remove this function, it is not being used anywhere 
async def file_exists(filename):
    path = '/path/to/directory/example.txt'
    if os.path.isfile(path):
        print('File exists')
    else:
        print('File does not exist')


# TODO: Have to find the right spot to put this, so that names have CST
async def zulu_to_cst(zulu_time_str):
    # create a datetime object representing the Zulu time
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


# TODO: function is here to show that layout window was passed as a parameter to this file
async def test_update_window(window):
    window['-SHOW LOGS-'].update(disabled = True)

if __name__ == "__main__":
    # Run the asyncio loop
    print('fr main program')
    asyncio.run(run())