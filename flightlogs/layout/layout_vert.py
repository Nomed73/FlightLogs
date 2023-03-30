#!/home/nm/dev/FlightLogs/venv python3
# download_file.py

import PySimpleGUI as sg
import os.path

sg.theme('DarkTeal6')

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
    [sg.Button("Show Logs", size=(sl_w, sl_h), pad=((b_pad_left,0),(0,0)), key='-SHOW LOGS-', disabled=False)], 
    
    # [sg.Button("Show Logs", key = '-SHOW LOGS-')],    
    [sg.Text('ULOG', size=(30,1)), sg.Text('SIZE', size=(10,1))],
    [sg.Listbox(values=[], enable_events=True, size=(40, 10), key="-LOG LIST-")],
    [sg.Text('ULogs available on drone\n', visible=False, key='-ULOGS-')],

]

status_view = [
    [sg.Text('Status...')],
    [sg.Text('File downloading...please wait', visible= False, key='-DOWNLOADING-') ],
]

# GUI design for buttons in horizontal view

# Button size and information
bv_w = 16
bv_h = 1
bv_pad_l=0
bv_pad_r = 5
bv_pad_t = 5
bv_pad_b = 5
# button_style = f'size=({bv_w} , {bv_h}), pad=(({bv_pad_l},{bv_pad_r}),({bv_pad_t}, {bv_pad_b}))'

buttons_vert = [
    [sg.Text('Options', size=(bv_w , bv_h), pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), justification='left')],
    [sg.Button("Connect Drone", size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-CONNECT-', disabled=False)], 
    [sg.Button('Save log', size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-SAVE LOG-', disabled=True)],
    [sg.Button('Save as CSV', size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-TO CSV-', disabled=True)],
    [sg.Button('Save as JSON',  size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-TO JSON-', disabled=True)],
    [sg.Button('View Flight Review', size=(bv_w , bv_h),  pad=((bv_pad_l,bv_pad_r),(bv_pad_t, bv_pad_b)), key = '-FLIGHT REVIEW-', disabled=True)],
    [sg.Text('Flight Review will open in browser', visible=False, key = '-CHECK BROWSER-')],
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
    [sg.Text('ULOG', size=(30,1)), sg.Text('SIZE', size=(10,1))],
    [sg.Listbox(values=[], enable_events=True, size=(50, 15), pad=((list_p_l, list_p_r),(list_p_t, list_p_b)), key="-LOG LIST-")],
    [sg.Text('ULogs available on drone\n', visible=False, key='-ULOGS-')],
]

status_view = [
    [sg.Text('Download status...')],
    [sg.Text('All files saved in ../Downloads/FlightLogs/', visible=False, key='-SAVE LOC-')], 
]

progress_bar= [
    [sg.ProgressBar(100, orientation='h', bar_color=('blue', 'white'), expand_x=True, size=(40, 20),  key='-PBAR-')],
    [
        sg.Text('', key='-OUT-', enable_events=True, font=('Arial Bold', 12), justification='left'),
        sg.Text('%', font=('Arial Bold', 12), justification='left'),
    ]
]

busy = [
    # [sg.Text('Downloading in progress...please wait', visible=False, key = '-DOWNLOADING-')],
    [sg.Text('Download DONE', visible=False, key = '-DONE-')],
    # [sg.Image(filename = 'flightlogs/assets/busy.gif', visible=False, key="-BUSY-")]
]



# create the layout for the gui
layout_vert = [
    [
        sg.Column(buttons_vert, size= (200, 300), vertical_alignment = 'top', key = '-SELECTIONS-'),
        sg.VSeparator(),
        sg.Column(file_view, size=(300, 300), vertical_alignment = 'top'),
    ],
    [ sg.HorizontalSeparator() ],
    [ sg.Column(status_view, size=(400, 100)) ],
    [ sg.Column(busy,  size=(400, 100))],
    # [ sg.Column(progress_animation)],
    # [ sg.Column(progress_bar) ],
]



