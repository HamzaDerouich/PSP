import threading
import time
from Descarga import Descarga

hilo1 = threading.Thread(target=Descarga("Musica", 6).run)
hilo2 = threading.Thread(target=Descarga("Video", 10).run)

hilo1.start()
hilo2.start()

hilo1.join()
print("Descarga de Musica finalizada")
hilo2.join()
print("Descarga de Video finalizada")

