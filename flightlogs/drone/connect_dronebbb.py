#!/home/nm/dev/FlightLogs/venv python3
# - /usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.ftp import FtpError
import sys
import subprocess

async def connect_drone():

    

    drone = System()
    await drone.connect(system_address="udp://:14550")


    # await drone.ftp.create_directory('THISONE')


    ftp_path = '/log/'
    # ftp_path01 = '/home/nm/Downloads/FlightLogs/'
    # ftp_list_dir = await drone.ftp.list_directory(ftp_path)
    # ftp_download = drone.ftp.download('/log/sess001/Flog001.ulg', '/home/nm/Downloads/FlightLogs/')
    # print("ftp_list_dir string", ftp_list_dir)

    # ftp_list_dir = await drone.ftp.list_directory(ftp_path)
    # print("List of items in log folder: ")
    # for item in ftp_list_dir:
    #     print(item)
    ftp_directory_path = '/log/'
    log_name_list = []
    try: 
        ftp_list_dir = await drone.ftp.list_directory(ftp_directory_path)
        print("List of items in log folder: ")
        for directory in ftp_list_dir:
            if "sess" in directory:
                ftp_log_path = '/log/' + directory[1:]
                ftp_list_logs = await drone.ftp.list_directory(ftp_log_path)
                for log in ftp_list_logs:
                    if ".ulg" in log:
                        print("Directory = ", directory[1:], "\tLog Type = ",log[1:11])
                        log_path = directory[1:]+'/'+log[1:11]
                        log_name_list.append(log_path)

    except FtpError as e:
        print(f"FTP Error: {e}")
    
    print(log_name_list)
    log_name_list.sort(reverse=True)
    print(log_name_list)
    # px4_directory = '/home/nm/dev/PX4-Autopilot'
    # run_px4 = f'cd {px4_directory} &&  make px4_sitl jmavsim'
    # px4_process = subprocess.call(['gnome-terminal', '--', 'bash', '-c', run_px4])


    #THIS FUCKING WORKS
    password = 'oelinux123'
    log002_path = '/data/px4/log/'+log_name_list[0]
    download_folder = '/home/nm/Downloads/FlightLogs/'
    run_scp = f'sshpass -p {password} scp -r root@192.168.0.113:{log002_path} {download_folder}'
    download_process = subprocess.call(['gnome-terminal', '--', 'bash', '-c',run_scp])
    print(download_process)

    # try: 
    #     previous_progress = -1
    #     async for progress in drone.ftp.download('/log/sess002/log001.ulg', '/home/nm/Downloads/FlightLogs/'):
    #         new_progress = round(progress.bytes_transferred/progress.total_bytes * 100)
    #         if new_progress != previous_progress:
    #             sys.stdout.write(f"\r{new_progress}%")
    #             sys.stdout.flush()
    #             previous_progress = new_progress

    # except FtpError as e:
    #     print(f"Download error: {e}")



    # async for log in drone.ftp.download('/log/sess001/Flog001.ulg\t3706379', '/home/nm/Downloads/FlightLogs/'):
    #     print(log)
    # drone.ftp.download('/data/px4/log/sess002/log001.ulg', '/home/nm/Downloads/FlightLogs/')


    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break
    
    print('Drone = ', drone)

    return drone

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(connect_drone())