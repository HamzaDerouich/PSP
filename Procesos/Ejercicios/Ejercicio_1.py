#Ejercicio Uno
import subprocess
import psutil
import time

## Función que lanza la calculadora 
def LanzarCalculadora():
    ruta = "notepad.exe"
    lanzar = subprocess.Popen([ruta])
    datos =  psutil.Process(lanzar.pid) 
    print(f"Proceso en ejecución en ruta: {ruta} ")
    print(f"Datos del proceso: {datos} ")
    MostrarInformacionProceso(lanzar.pid)
    CerrarProceso(lanzar)
    
def  MostrarInformacionProceso(pid):
    if psutil.pid_exists(pid):
        p = psutil.Process(pid) 
        usuario = p.username()  # Usuario que ejecuta el proceso
        nombre = p.name()  # Nombre del proceso
        estado = p.status()  # Estado del proceso (ejecutándose, detenido, etc.)
        memoria = p.memory_info()  # Uso de memoria
        cpu_porcentaje = p.cpu_percent(interval=1)  # Porcentaje de uso de CPU
        tiempo_creacion = p.create_time()  # Hora de creación del proceso
        hijos = p.children()  # Procesos hijos
        
        print(f"Información del proceso con PID {p}:")
        print(f"Usuario: {usuario}")
        print(f"Nombre: {nombre}")
        print(f"Estado: {estado}")
        print(f"Memoria (RSS/VMS): {memoria.rss / (1024 * 1024):.2f} MB / {memoria.vms / (1024 * 1024):.2f} MB")
        print(f"Uso de CPU: {cpu_porcentaje}%")
        print(f"Hora de creación: {tiempo_creacion}")
        print(f"Procesos hijos: {[child.pid for child in hijos]}")
        
    else:
        print("El proceso no existe!!")
     
# Función que termina un proceso en un timepo
def CerrarProceso(proceso):
    time.sleep(5)
    try:
        proceso.kill()
        print("Calculadora cerrada.")
    except Exception as e:
        print(f"No se pudo cerrar el proceso: {e}")
   
LanzarCalculadora()