import threading
import time

def sum(name, value):
    for i in range(0, value):
        print(f"{name}:{i}")
    
th1 = threading.Thread(target=sum, args=("Thread 1", 10))
th2 = threading.Thread(target=sum, args=("Thread 2", 10))

th1.start()
th2.start()

print("main thread")

th1.join()
th2.join()
