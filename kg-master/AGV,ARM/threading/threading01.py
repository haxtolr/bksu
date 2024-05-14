import threading
import time

def thread_1():
    while True:
        print("Thread 1 is running")
        time.sleep(1.0)

th1 = threading.Thread(target=thread_1)
th1.start()

while True:
    print("Main thread is running")
    time.sleep(2.0) 