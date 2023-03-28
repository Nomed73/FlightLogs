

import paramiko
import time
from mavsdk import System
import asyncio

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Server info
host = '192.168.0.113'
port_use = 22
user = 'root'
passwd = 'oelinux123'

# connect to the server
ssh.connect(hostname = host, username = user, password = passwd)

# async def connect_drone():
#     print('trying to connect...')
#     host = '192.168.0.113'
#     system = System(mavsdk_server_address = host)
#     try:
#         connected = await system.connect()
#         print('connected = ', connected)
#     except ConnectionError as error:
#         print(f'Connection failed: {error}')
    


# if __name__ == "__main__":
#     # Run the asyncio loop
#     asyncio.run(connect_drone())


# open an ftp connection with px4
sftp_client = ssh.open_sftp()

# list the operations that exist in the client
print('\ndir(sftp_client) : ')
print(dir(sftp_client))

# get current working directorycd _log
print("\nlistdir : ")
print(sftp_client.listdir() )

#
# print("\nCurrent directory : ")
# print(sftp_client.getcwd())

# # creates an interactive shell via wifi
# while True:
#     try: 
#         cmd = input('$> ')
#         if cmd == 'exit' : break
#         stdin, stdout, stderr = ssh.exec_command(cmd)
#         print(stdout.read().decode())
#     except KeyboardInterrupt:    
#         break

# stdin, stdout, stderr = ssh.exec_command('ls -a')
# print(stdout.read().decode())

# stdin, stdout, stderr = ssh.exec_command('ifconfig')
# print(stdout.read().decode())

# stdin, stdout, stderr = ssh.exec_command('voxl-wifi')
# print(stdout.read().decode())

print("will be closing all connections in 3 seconds")
for x in range(3,0,-1):
    print(x)
    time.sleep(1)
stdin.close()
stdout.close()
stderr.close()
sftp_client.close()
ssh.close()