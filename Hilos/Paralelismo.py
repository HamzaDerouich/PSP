import threading
import time

def escribeX():
    for i in range(1000):
        print("x",end="")
        time.sleep(0.001)
    return


def escribeY():
    for i in range(1000):
        print("y",end="")
        time.sleep(0.001)
    return


x = threading.Thread(target=escribeX)
x.start()
y = threading.Thread(target=escribeY) 
y.start()