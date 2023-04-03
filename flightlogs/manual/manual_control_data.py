#!/usr/bin/env python3

"""
This example shows how to use the manual controls plugin.
Note: Manual inputs are taken from a test set in this example to decrease complexity. Manual inputs
can be received from devices such as a joystick using third-party python extensions
Note: Taking off the drone is not necessary before enabling manual inputs. It is acceptable to send
positive throttle input to leave the ground. Takeoff is used in this example to decrease complexity
"""

import asyncio
import random
from mavsdk import System
import numpy as np


# Test set of manual inputs. Format: [roll, pitch, throttle, yaw]
manual_inputs = [
    [0, 0, 0.5, 0],  # no movement
    [-1, 0, 0.5, 0],  # minimum roll
    [1, 0, 0.5, 0],  # maximum roll
    [0, -1, 0.5, 0],  # minimum pitch
    [0, 1, 0.5, 0],  # maximum pitch
    [0, 0, 0.5, -1],  # minimum yaw
    [0, 0, 0.5, 1],  # maximum yaw
    [0, 0, 1, 0],  # max throttle
    [0, 0, 0, 0],  # minimum throttle
]

data = np.genfromtxt('/home/nm/dev/manual_flight/manual_flight/manual/flight_data.csv', dtype = float, delimiter =',', names = True)
async def manual_controls(cd):
    """Main function to connect to the drone and input manual controls"""
    # Connect to the Simulation
    drone = await cd.connect_drone()

    # # This waits till a mavlink based drone is connected
    # print("Waiting for drone to connect...")
    # async for state in drone.core.connection_state():
    #     if state.is_connected:
    #         print(f"-- Connected to drone!")
    #         break

    # Checking if Global Position Estimate is ok
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position state is good enough for flying.")
            break

    # set the manual control input after arming
    await drone.manual_control.set_manual_control_input(
        float(0), float(0), float(0.5), float(0)
    )

    # Arming the drone
    print("-- Arming")
    await drone.action.arm()

    # Takeoff the vehicle
    print("-- Taking off")
    await drone.action.takeoff()
    await asyncio.sleep(5)

    # set the manual control input after arming
    await drone.manual_control.set_manual_control_input(
        float(0), float(0), float(0.5), float(0)
    )

    # start manual control
    print("-- Starting manual control")
    await drone.manual_control.start_position_control()

    # counter for testing
    counter = 0

    print(data)
    while True:

        print(f'counter : {counter}')
        

        #get the data from the data file
        input_list = (data[counter])
        x = float(input_list[0])
        y = float(input_list[1])
        z = float(input_list[2])
        r = float(input_list[3])

        print(f'x = {x}, \ty = {y}, \tz = {z}, \tr = {r}')

        await drone.manual_control.set_manual_control_input(x, y, z, r)
        # await drone.manual_control.set_manual_control_input(roll, pitch, throttle, yaw)

        #Testing functional control for movement
        # await left(drone, 1.0)
        # await asyncio.sleep(0.1)
        # await left_right(drone, -1)
        # await forward_back(drone, -1.0)
        # await up_down(drone, 0.7)
        # await rotate(drone, -0.5)
        await asyncio.sleep(0.1)
        
        counter = counter + 1
        if counter >= data.size:
            break

    print('Landing...')
    await drone.action.land()
    await asyncio.sleep(2)

    # # this while loop is the original code. Making some changes above to see how it works.
    # while True:
    #     # grabs a random input from the test list
    #     # WARNING - your simulation vehicle may crash if its unlucky enough
    #     input_index = random.randint(0, len(manual_inputs) - 1)
    #     input_list = manual_inputs[input_index]

    #     # get current state of roll axis (between -1 and 1)
    #     roll = float(input_list[0])
    #     # get current state of pitch axis (between -1 and 1)
    #     pitch = float(input_list[1])
    #     # get current state of throttle axis (between -1 and 1, but between 0 and 1 is expected)
    #     throttle = float(input_list[2])
    #     # get current state of yaw axis (between -1 and 1)
    #     yaw = float(input_list[3])

    #     await drone.manual_control.set_manual_control_input(roll, pitch, throttle, yaw)

    #     await asyncio.sleep(0.1)



async def left_right( drone, y ):
    await drone.manual_control.set_manual_control_input(0.0, float(y), 0.5, 0.0)
    # await asyncio.sleep(0.1)

async def forward_back( drone, x ):
    await drone.manual_control.set_manual_control_input(float(x), 0.0, 0.5, 0.0)
    # await asyncio.sleep(0.1)

async def up_down(drone, z):
    await drone.manual_control.set_manual_control_input(0.0, 0.0, float(z), 0.0)
    # await asyncio.sleep(0.1)

async def rotate(drone, r):
    await drone.manual_control.set_manual_control_input(0.0, 0.0, 1.0, float(r))
    # await asyncio.sleep(0.1)




if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(manual_controls())
