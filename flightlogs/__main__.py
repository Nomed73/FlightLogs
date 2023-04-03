#!/home/nm/dev/FlightLogs/venv python3

'''
Display the ulog files for a connected drone. 
User selects a file and has the option to 
1. download ulog
2. download csv of vehicle_attitude message data
3. download json of vehicle_attitude message data
4. view ulog data in a local build of Flight Review
'''


import asyncio
import psutil

import PySimpleGUI as sg

import drone.connect_drone as cd
import layout.layout_vert as lt
import logs.flightreview as fr



async def main():
    # create the layout for the gui
    window = sg.Window("Drone Connect", 
                        lt.layout_vert,
                        size=(800,600), 
                        margins=(15, 15), 
                        resizable=True, 
                        element_justification='left')

    # Connect to drone - Initiate before window creation.
    drone = await cd.connect_drone()
    await fr.run(drone)

    async def locate_log():
        # Update status window and return ulog to download
        
        window['-STATUS-'].update(visible=True)
        window['-DONE-'].update(visible = False)
        window.refresh()
        selected_item = values['-LOG LIST-'][0]
        return logs.index(selected_item)

    async def update_window():
        # Update status window after download of file.
            
        window['-STATUS-'].update(visible = False)
        window['-DONE-'].update(visible = True)
        window.refresh()
        

    while True:
        event, values = window.read() # type: ignore
        
        if event == "-EXIT-" or event == sg.WIN_CLOSED:
            #Kills any possible running processes before exiting
            
            processes = psutil.process_iter()
            for process in processes:
                description = str(process.cmdline())
                try:
                    if "PX4" in description: process.kill()
                    if "jmavsim" in description: process.kill()
                    if "FlightLogs" in description: process.kill()
                    if "scp" in description: process.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            break

        if event == '-CONNECT-':
            #Connect the drone and list the files on the drone and enable buttons.
            
            logs = await fr.entries_to_list() 
            window['-LOG LIST-'].update(values = logs)
            window['-SAVE LOG-'].update(disabled = False)
            window['-TO CSV-'].update(disabled = False)
            window['-TO JSON-'].update(disabled = False)
            window['-FLIGHT REVIEW-'].update(disabled = False)
            window['-ULOGS-'].update(visible=True)

        elif event == '-SAVE LOG-':
            # Save selected ulog
            
            index_log = await locate_log()
            await fr.download_log(drone, index_log)
            await update_window()
            
        elif event == '-TO CSV-':
            # Download selected ulog to csv - vehicle_attitude message only
            
            index_log = await locate_log()
            await fr.create_csv(drone, index_log)
            await update_window()
            
        elif event == '-TO JSON-':
            # Download selected ulog to csv - vehicle_attitude message only
            
            index_log = await locate_log()
            await fr.create_json(drone, index_log)
            await update_window()
            
        elif event == '-FLIGHT REVIEW-':
            #Send ulog to Flight Review app for graphical display of data
            
            index_log = await locate_log() 
            window['-CHECK BROWSER-'].update(visible=True)
            await fr.upload_to_flight_review(drone, index_log)

    window.close()


if __name__ == "__main__":
    asyncio.run(main())
