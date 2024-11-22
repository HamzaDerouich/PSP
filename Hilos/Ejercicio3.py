import threading
import time

palabras = ["hola", "adios", "buenos dias", "buenas tardes", "buenas noches",]

def imprimirPalabra(contador):
    print(f"Palabra {contador}: {palabras[contador]}")
    

for i in range(len(palabras)):
    time.sleep(1)
    a = threading.Thread(target=imprimirPalabra , args=(i,))
    a.start()
    
