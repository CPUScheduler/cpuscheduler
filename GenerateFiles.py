import numpy as np

# Format:
#    PID #, Arrival t, CPU t, IO t, CPU t, IO t, CPU t
#    PID #, Arrival t, CPU t
#    PID #, Arrival t, CPU t, IO t, CPU t, IO t

np.random.seed(0)

if __name__ == "__main__":
    #
    # Generate process files for running through the simulation
    #

    # Parameters for each file
    maxFiles = 10
    directory = "processes"
    count = 2000
    maxTime = 100
    maxSwitches = 5
    maxArrivalInc = 5

    for fn in range(0,maxFiles):
        with open(directory+"/" + str(fn) + ".txt", "w") as f:
            # Initialize for each file
            arrival = 0

            for pid in range(0, count):
                # How many times we have, starting with CPU and then alternating
                # between CPU and IO
                switches = np.random.randint(1,maxSwitches)

                # Choose how long after the last process arived to make this
                # process arrive
                arrival += np.random.randint(1,maxArrivalInc)

                # Create the proccess line
                l = []
                l.append(pid)
                l.append(arrival)

                for j in range(0,switches):
                    l.append(np.random.randint(1,maxTime))

                f.write(",".join(str(x) for x in l) + "\r\n")

    #
    # Generate example output file for initial plotting
    #
    with open(directory+"/example_output.csv", "w") as f:
        # Initialize for each file
        arrival = 0

        # Some maximum values for random number generation
        maxStarted = 100
        maxCompleted = 1000
        maxWaitQueues = 50
        maxExecuting = 500
        maxWaitIO = 10

        f.write("PID,Submitted,Started,Completed,Queues,Executing,IO\r\n")

        for pid in range(0, count):
            arrival += np.random.randint(1,maxArrivalInc)
            started = arrival + np.random.randint(1,maxStarted)
            completed = arrival + np.random.randint(1,maxCompleted)
            waitingQueues = np.random.randint(1,maxWaitQueues)
            executing = np.random.randint(1,maxExecuting)
            waitingIO = np.random.randint(1,maxWaitIO)

            # Create the proccess line
            l = []
            l.append(pid)
            l.append(arrival)
            l.append(started)
            l.append(completed)
            l.append(waitingQueues)
            l.append(executing)
            l.append(waitingIO)
            f.write(",".join(str(x) for x in l) + "\r\n")
