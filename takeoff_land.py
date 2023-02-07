import asyncio
from mavsdk import System
# import ...FlightLogs.drone.connect_drone as connect_drone
# from ...FlightLogs.drone.connect_drone import connect_drone
# from .drone.connect_drone import connect_drone
# import drone.connect_drone as connect_drone
import drone.connect_drone as cd



async def run():

    drone = await cd.connect_drone()

    status_text_task = asyncio.ensure_future(print_status_text(drone))
    
    # Takeoff and land mission starts here
    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(10)

    print("-- Landing")
    await drone.action.land()

    status_text_task.cancel()



async def print_status_text(drone):
    try:
        async for status_text in drone.telemetry.status_text():
            print(f"Status: {status_text.type}: {status_text.text}")
    except asyncio.CancelledError:
        return


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run())
    # Run the asyncio loop
    asyncio.run(run())