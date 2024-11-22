import threading
import time
import random

def saludar(nombre,numero):
    print(f"Hola {nombre}, tu numero es {numero}")  

for i in range(3):
    numero = random.randint(1,100)
    a1 = threading.Thread(target=saludar,args=("Damian",numero))
    a2 = threading.Thread(target=saludar,args=("Juan",numero))
    a3 = threading.Thread(target=saludar,args=("Pedro",numero))
    time.sleep(1)
    print("Iniciando ......")
    a1.start()
    time.sleep(1)
    a2.start()
    time.sleep(1)
    a3.start()