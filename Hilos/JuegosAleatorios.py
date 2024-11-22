import threading
import time, logging

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)-10s]: %(message)s')

def generarNumeroAleatorio():
    import random
    numeroAleatorio = random.randint(1, 100)
    return numeroAleatorio



def NumerosAleatorios():
    for i in range(5):
        numero = generarNumeroAleatorio()
        time.sleep(1)   
        logging.debug(f"Numero aleatorio generado {numero}")
        #print(f"Numero aleatorio generado {numero}")

a = threading.Thread(target=NumerosAleatorios)
a1 = threading.Thread(target=NumerosAleatorios)
a.start()
a1.start()