import threading
import time
import multiprocessing

def cuentaRegresivaHilos(tiempo):
    i = 0
    while i < tiempo:
        time.sleep(1)
        print(i)
        i = i + 1
  
  
a = threading.Thread(target=cuentaRegresivaHilos, args=(10,))
a.start()
a.join()
print("Finalizado")