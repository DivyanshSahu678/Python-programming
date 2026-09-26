#Day 97

#Understand the concept of multithreading in python

import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

#normal code 
time1= time.perf_counter()
# func(5)
# func(3)

#using thread
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])

t1.start()
t2.start()

t1.join()
t2.join()

time2 = time.perf_counter()
print(time2 - time1)