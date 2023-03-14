#!/usr/bin/env python3

# Download the ulog of the last drone (or simulator) flight
# and and display the data using FreeFlight App
import os
import asyncio
import subprocess
import PySimpleGUI as sg
import layout.layout as lt
import logs.flightreview as fr
import drone.connect_drone as cd


from pathlib import Path



async def launch_px4():
    px4_directory = '/home/nm/dev/PX4-Autopilot'
    run_px4 = f'cd {px4_directory} && HEADLESS=1 make px4_sitl jmavsim'
    process = subprocess.call(['gnome-terminal', '--', 'bash', '-c', run_px4])
    return process


async def main():

    # create the layout for the gui
    window = sg.Window("Drone Connect", 
                        lt.layout,
                        size=(800,400), 
                        margins=(25, 25), 
                        resizable=True, 
                        element_justification='left')

    # get current directory
    # curr_directory = os.getcwd()

    if await launch_px4() == 0:

        # connect to drone or simulator
        drone = await cd.connect_drone()
        
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
            
            elif event == '-SAVE LOG-':
                selected_item = values['-LOG LIST-'][0]
                index_log = logs.index(selected_item)
                log = await fr.download_log(drone, index_log)

                pass

            elif event == '-TO CSV-':
                selected_item = values['-LOG LIST-'][0]
                index_log = logs.index(selected_item)
                await fr.create_csv(drone, index_log)
                pass

            elif event == '-TO JSON-':
                selected_item = values['-LOG LIST-'][0]
                index_log = logs.index(selected_item)
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
                result = await fr.upload_to_flight_review(drone, index_log)
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

    else:
        print('Connecting to drone failed.')

    window.close()

if __name__ == "__main__":
    asyncio.run(main())
