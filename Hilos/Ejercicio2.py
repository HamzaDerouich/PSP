import threading;
import time;



def mostrar(a,b):
    if a > b:
        print("0")
    else:
        time.sleep(1)
        for i in range(a,b+1):
            print(i,end=" ")

n1 ,n2 = 10,20
print(f"La difernencia entre los numeros es {n1 - n2}")
t1 = threading.Thread(target=mostrar, args=(n1,n2))
t1.start()

