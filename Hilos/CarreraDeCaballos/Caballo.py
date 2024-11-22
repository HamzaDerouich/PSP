import threading
import time
import random

class Caballo:
    ganador = None 

    def __init__(self, nombre):
        self.nombre = nombre
        self.llego = False  

    def correr(self):
        avance = random.randint(1, 3)
        return avance
        
    