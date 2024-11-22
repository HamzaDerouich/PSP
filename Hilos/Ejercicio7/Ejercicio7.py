import threading
import time
from Contador import Contador

hilo1 = threading.Thread(target=Contador(10).run)
hilo2 = threading.Thread(target=Contador(20).run)

hilo1.start()
hilo2.start()