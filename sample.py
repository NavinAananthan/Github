from timeit import default_timer as timer
import time

def elapsedtime():
    start = timer()
    print(23*2.3)
    end = timer()
    print(end - start)


# This python program is a sample demo how git works

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

elapsedtime()
countdown(5)