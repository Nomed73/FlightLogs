import asyncio
from mavsdk import System

async def run():
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyUSB0:921600")

    async for component in drone.components:
        if component.component_type == "VOXL":
            voxl2 = component
            break

    print(f"VOXL2 name: {voxl2.name}")
    print(f"VOXL2 ID: {voxl2.component_id}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
