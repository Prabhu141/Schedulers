import pycron
import time

def job():
    timenow = time.localtime()
    print("I'm working...", str( time.strftime("%H:%M", timenow) )) 

while True:
#                     |----------------- on minute 0, so every full hour
#                     |  |--------------- on hours 9 till 16
#                     |  |   | |-------- every day in month and every month
#                     V  V   V V  v------ on weekdays Monday till Friday
    #if pycron.is_now('0 9-16 * * mon-fri'):
    if pycron.is_now('0 9-16 * * mon-fri'):
        job()
    time.sleep(6)

# import pycron
# import time

# def job():
#     timenow = time.localtime()
#     print("I'm working...", str(time.strftime("%H:%M", timenow)))

# while True:
#     if pycron.is_now('* * * * *'):
#         job()
#     time.sleep(60)
