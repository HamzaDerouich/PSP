import threading 
import time
import random

# Semaforo para generar números aleatorios
suma = False
semaforo_gestionar_hilos = threading.Semaphore(1)

# Función que generará un número aleatorio entre 1 y 100 y los almacena en un lista

numeros = []
def generarNumeroAleatorio():
    fin = True if suma >= 20000  else False
    while fin != True:
        semaforo_gestionar_hilos.acquire()
        with threading.Lock():
            numeroAleatorio = random.randint(1, 100)
            numeros.append(numeroAleatorio)
    semaforo_gestionar_hilos.release()    

# Función que recorre la lista y los números terminados en 0 se sustituyen por 1

def recorrerLista():
    fin = True if suma >= 20000  else False
    if fin != True:
        for i in numeros:
            semaforo_gestionar_hilos.acquire()
            with threading.Lock():
                if i % 10 == 0:
                    numeros[numeros.index(i)] = 1
        semaforo_gestionar_hilos.release

# Función que suma los números de la lista y detendra los hilos anteriores cuando el valor super 20000

def sumarNumeros():
    suma_numeros = 0
    for i in numeros:
        suma_numeros = suma_numeros + i
        if suma_numeros >= 20000:
            suma = True

# Gestion de hilos

hilo_generarNumeroAleatorio = threading.Thread(target=generarNumeroAleatorio)
hilo_recorrerLista = threading.Thread(target=recorrerLista)
hilo_sumarNumeros = threading.Thread(target=sumarNumeros)

hilo_generarNumeroAleatorio.start()
hilo_recorrerLista.start()
hilo_sumarNumeros.start()