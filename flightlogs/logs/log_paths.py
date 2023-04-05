#!/home/nm/dev/FlightLogs/venv python3

'''
Create the a list of the files in the data/px4/log/ directory in the PX4
This list is created to retrieve the path of the logs. The path of the 
logs is required for the scp download. The path of the selected ulog
is returned. 
'''



import asyncio

from mavsdk.ftp import FtpError

import constants



async def get_ulogs(drone, index):
    # Return a list of the paths of the ulogs on the px4

    log_list = []
    try: 
        ftp_list_dir = await drone.ftp.list_directory(constants.FTP_DIR_PATH)
        for directory in ftp_list_dir:
            if "sess" in directory:
                ftp_log_path = '/log/' + directory[1:]
                ftp_list_logs = await drone.ftp.list_directory(ftp_log_path)
                for log in ftp_list_logs:
                    if ".ulg" in log:
                        log_path = directory[1:]+'/'+log[1:11]
                        log_list.append(log_path)

    except FtpError as e:
        print(f"FTP Error: {e}")

    log_list.sort(reverse=True)

    return log_list[index]

if __name__ == "__main__":
    asyncio.run(get_ulogs())