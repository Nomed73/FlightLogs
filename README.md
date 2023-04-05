# FlightLogs






#1 Prepare directory for Project
Crate a directory for the project. This directory will 

Installing Depencies:
pip3 install -r requirements.txt

Folders
data - storage for any data that some of the files may download, such as flight logs, teletemtry data, or custom data from the drone

telemetry - scripts that read telemetry data from drone

logs - scripts that download logs from the drone

missions - scripts for drone missions

drone - script to connect to drone


# Install virtual environment
Generally, the following order is the most appropriated.

    $ git clone <Project A>  # Cloning project repository
    $ cd <Project A> # Enter to project directory
    $ python3 -m venv my_venv # If not created, creating virtualenv
    $ source ./my_venv/bin/activate # Activating virtualenv
    (my_venv)$ pip3 install -r ./requirements.txt # Installing dependencies
    (my_venv)$ deactivate # When you want to leave virtual environment

All installed dependencies at step 5 will be unavailable after you leave virtual environment.