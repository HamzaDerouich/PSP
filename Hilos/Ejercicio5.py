import threading
import time

def quienEjecutaElHilo():
    if threading.current_thread() == threading.main_thread():
        print("El hilo principal es ejecutado")
    else:
        print("El hilo secundario es ejecutado")
    
print("Ejuecutando el hilo principal ......")
quienEjecutaElHilo()
time.sleep(1)
print("Ejuecutando el hilo secundario ......")
a = threading.Thread(target=quienEjecutaElHilo)
a.start()