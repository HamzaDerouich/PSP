import threading
import time
def tomaNombre(nombre):
    print("Name:",nombre)   
    time.sleep(2)
    
nombres = ["Damian","Juan","Pedro"]

for nombre in nombres:
    print("Iniciando ......")
    time.sleep(2)
    print("LLamada desde el thread ......")
    t = threading.Thread(target=tomaNombre,args=(nombre,))
    t.start()
    print("LLamada desde la funcion principal ......")
    tomaNombre(nombre)