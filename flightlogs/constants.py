import os

from pathlib import Path

# Constants that will need to be modified per user

# PATHS
'''
Paths
These are paths that are used. These paths will have to be modified depending on your
installation and preferences. 
'''

# FlightLogs directory in the Downloads folder - user can change the FlightLogs name
DOWNLOADS_PATH = 'Downloads/FlightLogs/'

# Path to the pyulog directory. Dependant on where user installed the pyulog package
PYULOG_DIR = '/home/nm/dev/FlightLogs/venv/lib/python3.8/site-packages/pyulog/'

# Path to installation of the Flight Review package part that would have to 
# adjusted is the /home/nm/dev section
FR_DIR = '/home/nm/dev/flight_review/app'



'''
PX4 and Drone
If you are using a different udp, user, password, ip address, update those here.
'''
# PX4 and drone, modify these accordint to your px4 and your settings
DRONE_ADDRESS = 'udp://:14550'
USER = 'root'
PASSWORD = 'oelinux123'
IP_ADDRESS = '192.168.0.113'

# The message data from the ulog that we want as a csv or JSON file.
DATA_MESSAGE = '-m vehicle_attitude '



'''
The constants below should NOT be changed. 
'''
# Users home directory plus the Downloads/FlightLogs/ DO NOT CHANGE
DOWNLOADS_DIR = os.path.join(str(Path.home() ), DOWNLOADS_PATH)

# these are internal paths on the px4, should not be changed. DO NOT CHANGE
FTP_DIR_PATH = '/log/'
ULOG_DIR = '/data/px4/log/'

# Empty list that will hold the names of the ulogs once the drone is connected DO NOT CHANGE
ENTRIES = {}








