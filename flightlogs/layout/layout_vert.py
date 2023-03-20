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



# Design of the GUI

# Layout for buttons in vertical format
# Button size and information
b_width = 15
b_height = 1
b_pad_left=1

buttons_vert = [
    # [sg.Button("Show Logs", size=(b_width, b_height), pad=((b_pad_left,0),(0,0)), key = '-SHOW LOGS-', disabled=False)], 
    [sg.Text('\n\nSelect one of the following: ')],
    [sg.Button('Save log', size=(b_width, b_height),  pad=((b_pad_left,0),(0,0)), key = '-SAVE LOG-', disabled=True)],
    [sg.Button('Save as CSV', size=(b_width, b_height),  pad=((b_pad_left,0),(0,0)), key = '-TO CSV-', disabled=True)],
    [sg.Button('Save as JSON',  size=(b_width, b_height),  pad=((b_pad_left,0),(0,0)), key = '-TO JSON-', disabled=True)],
    [sg.Text('Files saved in Downloads/FlightLogs/\n')],
    [sg.HorizontalSeparator()],
    [sg.Text("\nFlight Review Analysis")],
    
    [sg.Button('Send to Flight Review', size=(b_width, b_height),  pad=((b_pad_left,0),(0,0)), key = '-FLIGHT REVIEW-', disabled=True)],
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
layout_1 = [
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











# GUI design for buttons in horizontal view

# Button size and information
bv_w = 16
bv_h = 1
bv_pad_l=0
bv_pad_r = 5
bv_pad_t = 5
bv_pad_b = 5
button_style = f'size=({bv_w} , {bv_h}), pad=(({bv_pad_l},{bv_pad_r}),({bv_pad_t}, {bv_pad_b}))'

buttons_vert = [
    # [sg.Button("Show Logs", size=(bh_w , b_height), pad=((b_pad_left,0),(0,0)), key = '-SHOW LOGS-', disabled=False)], 
    [sg.Text('Options', size=(bv_w , bv_h), pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), justification='left')],
    # [sg.Button("Show Logs", button_style, key = '-SHOW LOGS-', disabled=False)], 
    [sg.Button("Show Logs", size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-SHOW LOGS-', disabled=False)], 
    [sg.Button('Save log', size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-SAVE LOG-', disabled=True)],
    [sg.Button('Save as CSV', size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-TO CSV-', disabled=True)],
    [sg.Button('Save as JSON',  size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-TO JSON-', disabled=True)],
    # [sg.Text('Files saved in Downloads/FlightLogs/\n')],
    # [sg.HorizontalSeparator()],
    # [sg.Text("\nFlight Review Analysis")],
    
    [sg.Button('View Flight Review', size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-FLIGHT REVIEW-', disabled=True)],
    [sg.Text('Flight Review will open in browser', visible=False, key = '-CHECK BROWSER-')],
    # [sg.Button('Delete all logs', key = '-DELETE LOGS-')],  
    [sg.Button('Exit', size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t+15, bv_pad_b-5)), key = '-EXIT-')],    
]


# show the log files
sl_w = 10
sl_h = 1
list_p_t = 5
list_p_b = 5
list_p_l = 5
list_p_r = 5
file_view = [
    # [sg.Button("Show Logs", size=(sl_w, sl_h), pad=((b_pad_left,0),(0,0)), key = '-SHOW LOGS-', disabled=False)], 
    
    # [sg.Button("Show Logs", key = '-SHOW LOGS-')],    
    [sg.Text('ULOG', size=(30,1)), sg.Text('SIZE', size=(10,1))],
    [sg.Listbox(values=[], enable_events=True, size=(50, 15), pad=((list_p_l, list_p_r),(list_p_t, list_p_b)), key="-LOG LIST-")],
    [sg.Text('ULogs available on drone\n', visible=False, key='-ULOGS-')],
]

status_view = [
    [sg.Text('Status...')],
    [sg.Text('All files saved in ../Downloads/FlightLogs/', visible=False, key='-SAVE LOC-')],
]

progress_bar= [
    [sg.ProgressBar(100, orientation='h', bar_color=('blue', 'white'), expand_x=True, size=(40, 20),  key='-PBAR-')],
    [
        sg.Text('', key='-OUT-', enable_events=True, font=('Arial Bold', 12), justification='left'),
        sg.Text('%', font=('Arial Bold', 12), justification='left'),
    ]
]


# create the layout for the gui
layout_vert = [
    [
        sg.Column(buttons_vert, expand_y=True, vertical_alignment = 'top', key = '-SELECTIONS-'),
        sg.VSeparator(),
        sg.Column(file_view, vertical_alignment = 'top'),
    ],
    [ sg.HorizontalSeparator() ],
    [ sg.Column(status_view) ],
    [ sg.Column(progress_bar) ],
]



