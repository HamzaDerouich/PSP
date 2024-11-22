import threading
import time

class Descarga(threading.Thread):
    def __init__(self, nombre, tiempoDescarga):
        super().__init__()  
        self.nombre = nombre
        self.tiempoDescarga = tiempoDescarga
    
    def mostrar_barra_descarga(self):
        caracteresDescargados = ""  
        for i in range(30):
            caracteresDescargados += "#" 
            print(f"{caracteresDescargados}", end="\r")
            time.sleep(0.3)
        print(f"{caracteresDescargados}")  
    
    def run(self):
        print(f"Descargando {self.nombre}")
        time.sleep(self.tiempoDescarga)
        self.mostrar_barra_descarga()  
        print(f"Descarga finalizada {self.nombre}")

