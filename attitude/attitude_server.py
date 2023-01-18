
#!/usr/bin/env python3

#

import os
import socket
import asyncio
from mavsdk import System
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Global variable - location of server
attitude_from_drone = './attitude_from_drone'

# Testing to see if it is necessary to have an async going
if __name__ == "__main__":

    #
    try:
        os.unlink(attitude_from_drone)
    except OSError:
        if os.path.exists(attitude_from_drone):
            raise

    #Initiate server
    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_socket.bind(attitude_from_drone)
    server_socket.listen()
    client_socket, address = server_socket.accept()
    msg = ''
    client_socket.send(bytes(msg, "utf-8")) 