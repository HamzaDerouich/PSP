import threading
import time

semaforo_conexion_base_de_datos = threading.Semaphore(4)

def conexionBaseDeDatos(i):
        print(f"Conexión base de datos {i}")
        semaforo_conexion_base_de_datos.acquire()
        with threading.Lock():
            print(f"Realizando la conexión base de datos {i}")
            time.sleep(1)
        semaforo_conexion_base_de_datos.release()

def ejecutar10Hilos():
    for i in range(10):
        a = threading.Thread(target=conexionBaseDeDatos,args=(i,))
        a.start()

ejecutar10Hilos()