#!/home/nm/dev/FlightLogs/venv python3
# - /usr/bin/env python3

import asyncio
from mavsdk import System
# import sys

async def connect_drone():

    

    drone = System()
    await drone.connect(system_address="udp://:14550")

    # testing connection to voxl2 using station mode
    # print(f'\n inside the connect_drone() function...')
    # voxl2_address = '192.168.0.113'
    # drone = System(mavsdk_server_address = voxl2_address, port=22)

    
    # await drone.connect(system_address=f"udp://{voxl2_address}:14551")

    # port that did not work: 14550, 22, 5760


    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    return drone

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(connect_drone())