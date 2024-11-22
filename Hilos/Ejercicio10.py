"""Ejercicio 10: Uso de Condition con wait y notify
Crea un programa en Python que simule una situación en la que dos hilos se alternan para
imprimir números. Un hilo imprimirá números impares y otro imprimirá números pares.
Utiliza un objeto Condition para la sincronización entre ambos hilos y asegúrate de que los
números se impriman de manera alternada.
Instrucciones:
● Usa la clase Condition de la biblioteca threading.
● Un hilo debe imprimir números impares del 1 al 9, y el otro, números pares del 2 al
10.
● Utiliza los métodos wait() y notify() para coordinar la impresión entre los hilos
"""
import threading
import time

# Función para imprimir números impares
def imprimir_numeros_pares(condicion):
    for i in range(1, 10):
        with condicion:
            condicion.wait()
            if i % 2 == 0:
                print(i)
            condicion.notify()
           
# Función para imprimir números impares
def imprimir_numeros_impares(condicion):
    for i in range(2, 11):
        with condicion:
            condicion.wait()
            if i % 2 != 0:
                print(i)
            condicion.notify()


#Crear condición
condicion = threading.Condition()

# Crear hilos
hilo_numeros_pares = threading.Thread(target=imprimir_numeros_pares , args=(condicion,))
hilo_numeros_impares = threading.Thread(target=imprimir_numeros_impares , args=(condicion,))

# Iniciar hilos
hilo_numeros_pares.start()
hilo_numeros_impares.start()

with condicion:
    condicion.notify()