#!/home/nm/dev/FlightLogs/venv python3
# download_file.py

import PySimpleGUI as sg
import os.path

sg.theme('DarkTeal6')


# # window layout in two columns
# file_list_column = [
#     [
#         # sg.Text("Ulog Files"), 
#         sg.Button("View ulogs", key = "-ULOGS-")
#         # sg.Listbox(values = entries, size=(20, len(entries)), key = '-LIST-', enable_events=True)
#         # sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
#         # sg.FolderBrowse(),
#     ],
#     [
#         sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")
#     ],
# ]

# # show the name of the file that was chosen
# image_viewer_column = [
#     [sg.Text("Select file from the left")],
#     [sg.Text(size=(40,1), key="-TOUT-")],
#     # [sg.FileSaveAs(key='-SAVE AS-')],
#     [sg.Button("Save file...", key = '-SAVE FILE-')],
#     [sg.Button("Delete...", key = "-DELETE-")],
#     [sg.Button("Flight Review", key = "-FLIGHT REVIEW-")],
# ]



#  GUI design for buttons in horizontal view

# Button size and information
bh_w = 15
bh_h = 1
bh_pad_l=1

buttons_hor = [
    # [sg.Button("Show Logs", size=(bh_w , b_height), pad=((b_pad_left,0),(0,0)), key = '-SHOW LOGS-', disabled=False)], 
    [sg.Text('\n\nSelect one of the following: ')],
    [sg.Button('Save log', size=(bh_w , bh_h),  pad=((bh_pad_l,0),(0,0)), key = '-SAVE LOG-', disabled=True)],
    [sg.Button('Save as CSV', size=(bh_w , bh_h),  pad=((bh_pad_l,0),(0,0)), key = '-TO CSV-', disabled=True)],
    [sg.Button('Save as JSON',  size=(bh_w , bh_h),  pad=((bh_pad_l,0),(0,0)), key = '-TO JSON-', disabled=True)],
    [sg.Text('Files saved in Downloads/FlightLogs/\n')],
    [sg.HorizontalSeparator()],
    [sg.Text("\nFlight Review Analysis")],
    
    [sg.Button('Send to Flight Review', size=(bh_w , bh_h),  pad=((bh_pad_l,0),(0,0)), key = '-FLIGHT REVIEW-', disabled=True)],
    [sg.Text('Flight Review will open in browser', visible=False, key = '-CHECK BROWSER-')],
    # [sg.Button('Delete all logs', key = '-DELETE LOGS-')],  
    # [sg.Button('Exit', size=(b_width, b_height), pad=((b_pad_left,0),(0,0)), key = '-EXIT-')], 
    
]


# show the log files
sl_w = 10
sl_h = 1
file_view = [
    [sg.Button("Show Logs", size=(sl_w, sl_h), pad=((b_pad_left,0),(0,0)), key = '-SHOW LOGS-', disabled=False)], 
    
    # [sg.Button("Show Logs", key = '-SHOW LOGS-')],    
    [sg.Text('ULOG', size=(30,1)), sg.Text('SIZE', size=(10,1))],
    [sg.Listbox(values=[], enable_events=True, size=(40, 10), key="-LOG LIST-")],
    [sg.Text('ULogs available on drone\n', visible=False, key='-ULOGS-')],
]

status_view = [
    [sg.Text('Status...')]
]


# create the layout for the gui
layout_hor = [
    [
        sg.Column(buttons_vert, expand_y=True, vertical_alignment = 'top', key = '-SELECTIONS-'),
        sg.VSeparator(),
        sg.Column(file_view, vertical_alignment = 'top'),
    ],
    [sg.HorizontalSeparator()],
    [
        sg.Text("\ntesting to see if its a new row"),
        sg.VSeparator(),
        sg.Column(status_view)
    ],
    [
        sg.Button('Exit', size=(b_width, b_height), pad=((b_pad_left,0),(0,0)), key = '-EXIT-')
    ], 

]



