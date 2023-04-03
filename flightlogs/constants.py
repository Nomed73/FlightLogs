import os

from pathlib import Path

# Constants that will need to be modified per user

# PATHS
'''
Paths
These are paths that are used. These paths will have to be modified depending on your
installation and preferences. There is no need to change #1 and #2. 
However #3 and #4 will have to change depending on your installations and directories.
'''

# 1.    FlightLogs directory in the Downloads folder - user can change the FlightLogs name
DOWNLOADS_PATH = 'Downloads/FlightLogs/'

# 2.    Users home directory plus the Downloads/FlightLogs/ 
DOWNLOADS_DIR = os.path.join(str(Path.home() ), DOWNLOADS_PATH)

# 3.    Path to the pyulog directory. Dependant on where user installed the pyulog package
PYULOG_DIR = '/home/nm/dev/FlightLogs/venv/lib/python3.8/site-packages/pyulog/'

# 4.    Path to installation of the Flight Review package part that would have to 
#       adjusted is the /home/nm/dev section
FR_DIR = '/home/nm/dev/flight_review/app'

'''
PX4 and Drone
Section 1 is to connect to the PX4. If you are using a different udp, user, password, 
ip address, update those here.
'''
# 1.    PX4 and drone, modify these accordint to your px4 and your settings
DRONE_ADDRESS = 'udp://:14550'
USER = 'root'
PASSWORD = 'oelinux123'
IP_ADDRESS = '192.168.0.113'

# these are internal paths on the px4, should not be changed. 
FTP_DIR_PATH = '/log/'
ULOG_DIR = '/data/px4/log/'

# The data from the ulog that we want as a csv or JSON file.
DATA_MESSAGE = '-m vehicle_attitude '


'''
Other
'''
# Empty list that will hold the names of the ulogs once the drone is connected
ENTRIES = {}








