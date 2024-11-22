import threading
import time
import random

diccionaro = {}

def generarNumeroAleatorio(id):
    total = 0
    for i in range(10):
       numeroAleatorio = random.randint(1, 100)
       total = total + numeroAleatorio
       
    diccionaro[id] = total
    return total

def ejecutar10Hilos():
    for i in range(10):
        a = threading.Thread(target=generarNumeroAleatorio,args=(f"Hilo:{i}",))
        a.start()

ejecutar10Hilos()
print("Numeros generados ......")
for i in diccionaro:
    print(f"Hilo {i} Total: {diccionaro[i]}")
nombre = ""
puntos = 0
print("Calculando el numero mayor ......")
for i in diccionaro:
    if diccionaro[i] > puntos:
        puntos = diccionaro[i]
        nombre = i
print(f"El numero aleatorio generado por el hilo {puntos} el mayor es {nombre}")
