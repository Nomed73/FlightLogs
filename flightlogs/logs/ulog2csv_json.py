# Download ulog file into a csv and a json file.
# 

import os
import csv
import json
import time



def create_csv():
    change_dir = '/home/nm/.local/lib/python3.8/site-packages/pyulog/'
    data_csv = '-m vehicle_attitude /home/nm/Documents/Testing_uLog_to_csv/log_1_2023-2-27-10-24-30.ulg'
    # get_all = '/home/nm/Documents/Testing_uLog_to_csv/log_1_2023-2-27-10-24-30.ulg'
    get_csv = 'python3 ulog2json.py ' + data_csv
    # get_csv = 'python3 ulog2json.py ' + get_all

    os.chdir(change_dir)
    os.system(get_csv)



def create_json():
    csv_path = "/home/nm/Documents/Testing_uLog_to_csv/log_1_2023-2-27-10-24-30_vehicle_attitude_0.csv"
    json_path = '/home/nm/Documents/Testing_uLog_to_csv/log_1_2023-2-27-10-24-30_vehicle_attitude_0.json'
    data = {}

    with open(csv_path, encoding = 'utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['timestamp']
            data[key] = rows

    with open(json_path, 'w', encoding = 'utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent = 4))

# Main program starts here
if __name__ == "__main__":

    start_time = time.time()

    print('Creating csv...')
    create_csv()
    print('CSV done...')
    print('Creating JSON...')
    create_json()

    end_time = time.time()
    print(f'Execution time : {end_time - start_time}')
