import threading
import time

def ThreadDiccionario(name,inicio = 1,fin = 3):
    for x in range(inicio,fin):
        print(f"Nombre: {name} y numero: {x}",end="")
        time.sleep(0.1)
        
nombres = ["Damian","Juan","Pedro"]
for nombre in nombres:
    print("Iniciando ......")
    time.sleep(2)
    print("LLamada desde el thread ......")
    t = threading.Thread(target=ThreadDiccionario,args=(nombre,),kwargs={"inicio":1,"fin":3})
    t.start()
    print("LLamada desde la funcion principal ......")
    ThreadDiccionario(nombre,1,2)