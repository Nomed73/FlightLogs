
'''
Simulate a mission where the download of the log starts after mission is complete. 

'''


import asyncio
from mavsdk import System
import logs_all_download
import connect_drone



async def run():

    drone = await connect_drone.connect_drone() 
    # System()
    # await drone.connect(system_address="udp://:14550")

    status_text_task = asyncio.ensure_future(print_status_text(drone))

    # print("Waiting for drone to connect...")
    # async for state in drone.core.connection_state():
    #     if state.is_connected:
    #         print(f"-- Connected to drone!")
    #         break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(5)

    print("-- Landing")
    await drone.action.land()

    async with (not drone.action.disarm()):
        #await start_download(drone)
        await logs_all_download.begin_download(drone)


    status_text_task.cancel()



# async def start_download(drone):
#     await logs_all_download.begin_download(drone)


async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    # asyncio.run(run())