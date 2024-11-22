import threading
import time
import random

capacidad = 10
productos = []

# Semáforos
semaforo_productor = threading.Semaphore(capacidad)  # Inicia con la capacidad total.
semaforo_consumidor = threading.Semaphore(0)         # Inicia en 0 porque no hay productos al comienzo.

# Lock para acceso concurrente a la lista de productos
lock = threading.Lock()

def productor():
    while True:
        num = random.randint(1, 100)
        semaforo_productor.acquire()  # Esperar a que haya espacio disponible.
        with lock:
            productos.append(f"Producto: {num}")
            print(f"Productor: Se ha añadido el producto a la cinta: {num} / capacidad: {len(productos)}/{capacidad}")
        semaforo_consumidor.release()  # Señalar que hay un producto disponible.
        time.sleep(random.uniform(0.1, 1))  # Simular tiempo de producción.

def consumidor():
    while True:
        semaforo_consumidor.acquire()  # Esperar a que haya un producto disponible.
        with lock:
            producto = productos.pop(0)
            print(f"Consumidor: Se ha consumido el producto: {producto} / capacidad: {len(productos)}/{capacidad}")
        semaforo_productor.release()  # Señalar que hay espacio disponible.
        time.sleep(random.uniform(0.1, 1))  # Simular tiempo de consumo.

# Crear y lanzar hilos
hilos = []
for _ in range(2):  # Dos productores
    h = threading.Thread(target=productor)
    hilos.append(h)
    h.start()

for _ in range(2):  # Dos consumidores
    h = threading.Thread(target=consumidor)
    hilos.append(h)
    h.start()

# Nota: Este código se ejecuta indefinidamente. Usa Ctrl+C para detenerlo.
 