import threading
import time
import random

# Variables compartidas
numeros = []
suma = 0
finalizar = False

# Lock para proteger las variables compartidas
lock = threading.Lock()

def generarNumeroAleatorio():
    global finalizar
    while not finalizar:
        numeroAleatorio = random.randint(1, 100)
        with lock:
            numeros.append(numeroAleatorio)
            print(f"Generado: {numeroAleatorio}")
        time.sleep(0.01)  

def recorrerLista():
    global finalizar
    while not finalizar:
        with lock:
            for i in range(len(numeros)):
                if numeros[i] % 10 == 0:
                    print(f"Reemplazado {numeros[i]} por 1")
                    numeros[i] = 1
        time.sleep(0.05)  

def sumarNumeros():
    global suma, finalizar
    while not finalizar:
        with lock:
            suma = sum(numeros)
            print(f"Suma actual: {suma}")
            if suma >= 20000:
                finalizar = True
        time.sleep(0.1)  

# Crear y lanzar los hilos
hilo_generarNumeroAleatorio = threading.Thread(target=generarNumeroAleatorio)
hilo_recorrerLista = threading.Thread(target=recorrerLista)
hilo_sumarNumeros = threading.Thread(target=sumarNumeros)

hilo_generarNumeroAleatorio.start()
hilo_recorrerLista.start()
hilo_sumarNumeros.start()

# Esperar a que los hilos finalicen
hilo_generarNumeroAleatorio.join()
hilo_recorrerLista.join()
hilo_sumarNumeros.join()

print("Proceso terminado.")
