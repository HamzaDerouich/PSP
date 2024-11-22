import threading
from Caballo import Caballo
import time
# Crear caballos
caballo1 = Caballo("Caballo1")
caballo2 = Caballo("Caballo2")


#Mostrar distancia de cada caballo
def mostrar_distancia(distancia_acutal):
    for i in range(distancia_acutal):
        print("#", end="")

meta = 20 ;

def carrera():
    # Crear los hilos para los caballos
    distacia_caballo1 = 0
    distacia_caballo2 = 0
    while True:
        hilo1 = threading.Thread(target=caballo1.correr)
        hilo2 = threading.Thread(target=caballo2.correr)

        hilo1.start()
        hilo2.start()
        time.sleep(1)

        # Caballo corriendo
        distacia_caballo1 = distacia_caballo1 + caballo1.correr()
        distacia_caballo2 = distacia_caballo2 + caballo2.correr()

        # Mostrar el progreso
        
        print("\n" + "="*40)  
        print("🚦 Carrera de Caballos 🚦".center(40))
        print("="*40)

        print(f"Caballo 1 🐎: {mostrar_distancia(distacia_caballo1)}")
        print(f"Caballo 2 🐎: {mostrar_distancia(distacia_caballo2)}")
        print("="*40)

        # Comparar distancias
        
        if distacia_caballo1 > distacia_caballo2:
            print(f"🔵 {caballo2.nombre} se acerca a {caballo1.nombre}")
        elif distacia_caballo2 > distacia_caballo1:
            print(f"🟢 {caballo1.nombre} se acerca a {caballo2.nombre}")
        else:
            print(f"🔴 {caballo1.nombre} y {caballo2.nombre} están igualados")

        # Revisar si algún caballo ha llegado a la meta
        
        if distacia_caballo1 >= meta:
            print(f"\n🎉 ¡{caballo1.nombre} GANA la carrera! 🎉")
            break
        elif distacia_caballo2 >= meta:
            print(f"\n🎉 ¡{caballo2.nombre} GANA la carrera! 🎉")
            break

        # Pausa para que el usuario vea el progreso
        
        time.sleep(0.5)


carrera()
