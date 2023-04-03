#!/home/nm/dev/FlightLogs/venv python3

'''
Creates a udp connection to the voxl/px4 on the 14550 port. 
returns the connected drone to __main__.py
'''

import asyncio

from mavsdk import System

import constants


async def connect_drone():

    drone = System()
    await drone.connect(system_address=constants.DRONE_ADDRESS)

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break
    
    return drone


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(connect_drone())