#! /usr/bin/python3

# 

import socket
import asyncio
from mavsdk import System
import errno

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#Global variable
attitude_from_drone = './attitude_from_drone'

# Main function, creates server connection and drone connection.
async def run():

    # Client socket establish connection with server socket
    client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)    
    client_socket.connect(attitude_from_drone)
    msg = client_socket.recv(1024)

    # Initiate the drone
    drone = System()
    await drone.connect(system_address="udp://:14550")
    asyncio.ensure_future(attitude(drone, client_socket))

# Receives the attitude data from the drone : [pitch, roll, yaw]   
#  and passes the data to the socket server     
async def attitude(drone, client_socket):
    async for euler in drone.telemetry.attitude_euler():
        msg =str([euler.pitch_deg, euler.roll_deg, euler.yaw_deg]).encode('utf-8')
        print(msg)
        try:
            client_socket.sendall(msg)
        except IOError as e:
            if e.errno == errno.EPIPE:
                pass


if __name__ == "__main__":

    #Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()