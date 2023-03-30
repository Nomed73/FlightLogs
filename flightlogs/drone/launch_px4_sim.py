#!/home/nm/dev/FlightLogs/venv python3

'''
Launch the PX4-Autopilot jmavsim. 
See note at bottom of where to place the code.
'''

import subprocess


async def launch_px4():
    # launch PX4 jmavsim

    # replace path with path to your PX4-Autopilot build
    px4_directory = '/home/nm/dev/PX4-Autopilot' 
    run_px4 = f'cd {px4_directory} &&  make px4_sitl jmavsim'
    px4_process = subprocess.call(['gnome-terminal', '--', 'bash', '-c', run_px4])
    return px4_process


'''
NOTE: 
If connecting to simulator for testing, place this code in main() 
before the while True loop, replace the two lines above it that connect to the drone. 
'''
#     # Verify that the px4 and sim are running
#     # if await launch_px4() == 0:
#     #     drone = await cd.connect_drone()
#     # else:
#     #     print('drone not connected