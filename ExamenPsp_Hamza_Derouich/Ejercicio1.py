"""
- Tema 1: Introducción a la programación multiproceso. Programación de procesos en Python
Criterios de calificación:
- Cada pregunta tiene un valor de 5 puntos. El valor de cada subapartado se indica en el enunciado.
- Para optar a la nota máxima en un apartado, se valorará positivamente el manejo de errores para evitar
que el programa se detenga inesperadamente, así como la inclusión de comentarios que faciliten la
lectura y comprensión del código.
Resultados de Aprendizaje:
- RA.1: Desarrolla aplicaciones compuestas por varios procesos reconociendo y aplicando principios de
programación paralela.
Nombre Alumno: Puntuación:
Ejercicio 1: Menú Interactivo: Realiza un programa que presente un menú interactivo en Python
que permita a los usuarios gestionar los procesos en su sistema operativo, utilizando las bibliotecas
subprocess y psutil para interactuar con los procesos. Debe contener las siguientes opciones:
- (1 pto) Listar todos los procesos en ejecución, mostrando el nombre, el PID, el estado y el
porcentaje de uso de CPU.
- (1 pto) Lanzar el Bloc de notas (‘Notepad.exe’) como un nuevo proceso.
- (1’5 ptos) Consultar la prioridad de un proceso que especifique el usuario por su PID.
Permitir al usuario realizar un cambio a BELOW_NORMAL_PRIORITY_CLASS si así lo
desea.
- (1 pto) Terminar un proceso que especifique el usuario por su PID.
- (0’5 ptos) Salir del programa"""

import subprocess
import psutil
import time

def listar_procesos():
    print("_____LISTADO_DE_PROCESOS_____")
    contador_procesos = 0;
    for procesos in psutil.process_iter(['name', 'pid', 'status', 'cpu_percent']):
      try:
          print(f"Proceso Nª {contador_procesos}")
          print(procesos)
          print("______________________________________")
          contador_procesos += 1
      except Exception as e:
          print(f"No se han podido listar los procesos: {e}")

def lanzar_bloc_de_notas():
    print("______LANZAR_PROCESOS______")
    try:
        proceso = subprocess.Popen(["notepad.exe"])
        print(f"Proceso lanzado correctamente con {proceso.pid}!!")
    except Exception as e:
        print(f"Error no se ha podido lanzar el proceso: {e}")

def consultar_prioridad():
    print("______PRIORIDAD_DE_PROCESOS_____")
    pid = int(input("Digite el PID del proceso: "))
    try:
        proceso = psutil.Process(pid)
        print(f"PID del proceso: {pid} , Prioridad: {proceso.nice()}")
        resultado = input("Para cambiar la prioridad digite s")
        if resultado.lower() == 's':
            proceso.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
            print(f"Prioridad del proceso {pid} cambiada !!")
    except Exception as e:
        print(f"No se ha podidido consultar la prioridad: {e}")

def terminar_proceso():
    print("______TERMINAR_PROCESOS_____")
    pid = int(input("Introduce el PID del proceso que deseas terminar: "))
    try:
        time.sleep(2)
        proceso = psutil.Process(pid)
        proceso.kill()
        print(f"Proceso con {pid}, terminado!!")
    except Exception as e:
        print(f"Error al terminar el proceso: {e}")

def menu():
    opcion = 0
    while True:
        print("\n_____GESTION_DE_PROCESOS_____:")
        print("1. Listar procesos")
        print("2. Lanzar Bloc de notas")
        print("3. Consultar y Cambiar prioridad de proceso")
        print("4. Terminar proceso")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            listar_procesos()
        elif opcion == '2':
            lanzar_bloc_de_notas()
        elif opcion == '3':
            consultar_prioridad()
        elif opcion == '4':
            terminar_proceso()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Datos no validos, vuelva a digitar los datos!!.")

menu()
