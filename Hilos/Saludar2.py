import threading
def actividad():
    print("Escribo un hilo")

print("INICIO")
hilos = []
for i in range(30):
     t =  threading.Thread(target=actividad)
     hilos.append(t)
     t.start()
     
print("Escribo en principal")
print(hilos)
