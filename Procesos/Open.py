import os
import subprocess

a = open(os.devnull,'w')

p = subprocess.call(['ipconfig'],stdout=a,stderr=subprocess.STDOUT)

if p == 0 :
    print("Proceso lanzado.")
    print(a)
else:
    print("Proceso no lanzado.")


