import time
import threading
class Contador (threading.Thread):
    limite = 0
    def __init__(self, limite):
        self.limite = limite

    def run(self):
        i = 1
        while i <= self.limite:
            print(f"Contador: {i}")
            i = i + 1
            time.sleep(1)
           