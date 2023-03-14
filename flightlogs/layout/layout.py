# download_file.py

import PySimpleGUI as sg
import os.path

sg.theme('DarkTeal6')


# window layout in two columns
file_list_column = [
    [
        # sg.Text("Ulog Files"), 
        sg.Button("View ulogs", key = "-ULOGS-")
        # sg.Listbox(values = entries, size=(20, len(entries)), key = '-LIST-', enable_events=True)
        # sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        # sg.FolderBrowse(),
    ],
    [
        sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")
    ],
]

# show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Select file from the left")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    # [sg.FileSaveAs(key='-SAVE AS-')],
    [sg.Button("Save file...", key = '-SAVE FILE-')],
    [sg.Button("Delete...", key = "-DELETE-")],
    [sg.Button("Flight Review", key = "-FLIGHT REVIEW-")],
]


# show the log files
file_view = [
    [sg.Text('ULogs available on drone')],
    # [sg.Button("Show Logs", key = '-SHOW LOGS-')],    
    [sg.Listbox(values=[], enable_events=True, size=(50, 20), key="-LOG LIST-")]
]

# Button size and information
b_width = 20
b_height = 1
b_pad_left=1

file_options = [
    [sg.Button("Show Logs", size=(b_width, b_height), pad=((b_pad_left,0),(0,0)), key = '-SHOW LOGS-', disabled=False)], 
    [sg.Text('\n\nSelect one of the following: ')],
    [sg.Button('Save log', size=(b_width, b_height),  pad=((b_pad_left,0),(0,0)), key = '-SAVE LOG-', disabled=True)],
    [sg.Button('Save as CSV', size=(b_width, b_height),  pad=((b_pad_left,0),(0,0)), key = '-TO CSV-', disabled=True)],
    [sg.Button('Save as JSON',  size=(b_width, b_height),  pad=((b_pad_left,0),(0,0)), key = '-TO JSON-', disabled=True)],
    [sg.Text('*Logs saved in Downloads/FlightLogs/\n')],
    [sg.Button('View in Flight Review', size=(b_width, b_height),  pad=((b_pad_left,0),(0,0)), key = '-FLIGHT REVIEW-', disabled=True)],
    [sg.Text('Check browser for Flight Review', visible=False, key = '-CHECK BROWSER-')],
    # [sg.Button('Delete all logs', key = '-DELETE LOGS-')],  
    [sg.Button('Exit', size=(b_width, b_height), pad=((b_pad_left,0),(0,0)), key = '-EXIT-')], 
    
]

# create the layout for the gui
layout = [
    [
        sg.Column(file_options, expand_y=True, vertical_alignment = 'top', key = '-SELECTIONS-'),
        sg.VSeparator(),
        sg.Column(file_view, vertical_alignment = 'top'),
    ]
]



