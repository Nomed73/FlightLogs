#!/home/nm/dev/FlightLogs/venv python3

'''
Components for the GUI layout
'''

import PySimpleGUI as sg

sg.theme('DarkTeal6')



# Button size and information
bv_w = 16
bv_h = 1
bv_pad_l=0
bv_pad_r = 5
bv_pad_t = 5
bv_pad_b = 5

# Buttons: user buttons for selections. 
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

# list box to show the files, the ulogs
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

# Messages for user, status updates
status_view = [
    [sg.Text('All files saved in ../Downloads/FlightLogs/', visible=True, key='-SAVE LOC-')], 
    [sg.Text('Status...', visible= True,)],
    
]

#Currenlty not used after switching to scp downloading.
progress_bar= [
    [sg.ProgressBar(100, orientation='h', bar_color=('blue', 'white'), expand_x=True, size=(40, 20),  key='-PBAR-')],
    [
        sg.Text('', key='-OUT-', enable_events=True, font=('Arial Bold', 12), justification='left'),
        sg.Text('%', font=('Arial Bold', 12), justification='left'),
    ]
]

# Display user friendly messages
busy = [
    # [sg.Text('Downloading in progress...please wait', visible=False, key = '-DOWNLOADING-')],
    [sg.Text('Download starting...please wait...', visible=False, key = '-STATUS-')],
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
]



