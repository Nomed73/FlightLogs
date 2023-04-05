# FlightLogs

A GUI interface to connect to the VOXL2/PX4 and be able to :
- download ulogs
- convert ulogs to csv
- convert csv to json
- view ulog in local Flight Review 

The csv and the JSON files are only for one message of the ulogs. Currently the data for the message '-m vehicle_attitude ' is downloaded. This message can be changed in the constants.py file. If there is enough interest or demand, a selection menu can be added so that the user can select which message data to download. 


# Prerequisite 
## Install Flight Review

Follow the Installation and Setup instructions here: https://github.com/PX4/flight_review
Preferably install the requirements.txt in a virtual environment. 

### Install virtual environment
Generally, the following order is the most appropriated.

    $ git clone <Project A>  # Cloning project repository
    $ cd <Project A> # Enter to project directory
    $ python3 -m venv my_venv # If not created, creating virtualenv
    $ source ./my_venv/bin/activate # Activating virtualenv
    (my_venv)$ pip3 install -r ./requirements.txt # Installing dependencies
    (my_venv)$ deactivate # When you want to leave virtual environment

All installed dependencies at step 5 will be unavailable after you leave virtual environment.

After running the python3 setup_db.py as per the instructions, please make a note of the absolute path to flight_review/app. This path is necessary in FlightLogs


## Install FlightLogs
 - Prepare directory to clone the FlightLogs repository
 - cd into the directory
 - Create a virtual environment. (see above)
 - Run pip3 install -r requirements.txt

## Using FlightLogs

Before the first use:
- Open the constants.py file and update the information there. 
- Activate the virtual environment.
- Open flightlogs and run '_main_.py'
- Click Connect Drone
- Choose any of the option

Flight Review will run on your default browser. It was tested in Firefox Developer edition.


# Issues
If there are any issues please submit them and I will fix as soon as I can.

Thanks. 

