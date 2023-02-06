#!/usr/bin/env python3

import asyncio
from mavsdk import System
import sys

async def connect_drone():
    drone = System()
    await drone.connect(system_address="udp://:14550")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    return drone

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(connect_drone())