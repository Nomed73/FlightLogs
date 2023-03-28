import psutil

processes = psutil.process_iter()

for process in processes:
    try:
        description = str(process.cmdline())
        # print(f'Type : {type(description)}\tDescription: {description}')
    
        if "PX4" in description:
            print(f'PX4 process: \t\t{description}')
        if "jmavsim" in description:
            print(f'jmavsim process: \t{description}')
        if "FlightLogs" in description:
            print(f'FlightLogs process: \t{description}')
        # else:
        #     print("No process with your description")    
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass