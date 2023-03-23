#!/home/nm/dev/FlightLogs/venv python3
# usr/bin/env python3

# Download the ulog of the last drone (or simulator) flight
# and and display the data using FreeFlight App
import asyncio
import subprocess
import PySimpleGUI as sg
import layout.layout_vert as lt
import logs.flightreview as fr
import drone.connect_drone as cd

from pathlib import Path


async def launch_px4():
    # Launch the PX4 simulator
    px4_directory = '/home/nm/dev/PX4-Autopilot'
    run_px4 = f'cd {px4_directory} && HEADLESS = 1 make px4_sitl jmavsim'
    px4_process = subprocess.call(['gnome-terminal', '--', 'bash', '-c', run_px4])
    return px4_process


async def main():
    # create the layout for the gui
    window = sg.Window("Drone Connect", 
                        lt.layout_vert,
                        size=(800,600), 
                        margins=(15, 15), 
                        resizable=True, 
                        element_justification='left')

    # # Verify that the px4 and sim are running
    # if await launch_px4() == 0:
    #     drone = await cd.connect_drone()
    # else:
    #     print('drone not connected')

    # Connect to drone
    drone = await cd.connect_drone()
    
    # Retrieve the system name parameter as a ParamValue object
    # system_name = drone.__dict__[
    # for key in system_name:
    #     print("\n",key, " : ", system_name[key])
    # print(drone.__dict__[mavsdk_server_address])

    # print("Drone name:", system_name)
    # print(f'Attempting to connect to drone : ')
    # drone = await cd.connect_drone()

    while True:
        event, values = window.read()

        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            break
    
        if event == '-SHOW LOGS-':
            # await fr.test_update_window(window)
            await fr.run(drone)
            logs = await fr.entries_to_list() 
            window['-LOG LIST-'].update(values = logs)
            window['-SAVE LOG-'].update(disabled = False)
            window['-TO CSV-'].update(disabled = False)
            window['-TO JSON-'].update(disabled = False)
            window['-FLIGHT REVIEW-'].update(disabled = False)
            window['-ULOGS-'].update(visible=True)
        
        elif event == '-SAVE LOG-':
            selected_item = values['-LOG LIST-'][0]
            index_log = logs.index(selected_item)
            window['-SAVE LOG-'].update(visible=True)
            log = await fr.download_log(drone, index_log, window)

        elif event == '-TO CSV-':
            selected_item = values['-LOG LIST-'][0]
            index_log = logs.index(selected_item)
            window['-SAVE LOG-'].update(visible=True)
            await fr.create_csv(drone, index_log)
            pass 

        elif event == '-TO JSON-':
            selected_item = values['-LOG LIST-'][0]
            index_log = logs.index(selected_item)
            window['-SAVE LOG-'].update(visible=True)
            await fr.create_json(drone, index_log)
            pass

        elif event == '-FLIGHT REVIEW-':
            #TODO Remove the print line
            print("Flight Review initiated...")

            #TODO - The next two lines of code are being repeated
            selected_item = values['-LOG LIST-'][0]
            index_log = logs.index(selected_item)
            window['-CHECK BROWSER-'].update(visible=True)
            # await fr.upload_to_flight_review(drone, index_log)
            result = await fr.upload_to_flight_review(drone, index_log,window)
            print(result)
            # if enable_notice:
            #     window['-CHECK BROWSER-'].update(visible=True)

        # elif event == '-DELETE LOGS-':
        #     await drone.log_files.erase_all_log_files()
        #     # logs = await fr.entries_to_list(drone) 
        #     logs = [[]]
        #     window['-LOG LIST-'].update(values = logs)
        #     # pass   

        # Run the asyncio loop
        # asyncio.run(fr.run(drone))

    # else:
    #     print('Connecting to drone failed.')

    window.close()

if __name__ == "__main__":
    asyncio.run(main())
