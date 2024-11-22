import threading
import time
def Saludar():
    time.sleep(1)
    print("Hola mundo, desde la funcion!!")

s = threading.Thread(target=Saludar)
s.start()
print("Hola mundo")
