import threading
import time

def Suma(a,b):
    print("Realizando suma ......")
    time.sleep(2)
    print(a+b)

s = threading.Thread(target=Suma,args=(2,2))
s.start()
