import subprocess

# Cambia la ruta si es necesario
ContadorPalabras = r"C:\Users\dam23\Desktop\PSP\ExamenPsp_Hamza_Derouich\ContadorPalabras.py"
ruta_archivo = r"C:\Users\dam23\Desktop\PSP\Procesos\Ejercicios\Fichero.txt"
ruta_archivo_temp = r"ExamenPsp_Hamza_Derouich/FicheroPalabras.txt"

with open(ruta_archivo,'r') as fichero_palabras:
    linea = fichero_palabras.readline()
    with open(ruta_archivo_temp,'w') as fichero_temp:
        escritor = fichero_temp.write(linea)


# Lanzar proceso
proceso = subprocess.Popen(
    ["python", ContadorPalabras],  
    stdout=subprocess.PIPE,    
    stdin=subprocess.PIPE,
    stderr=subprocess.PIPE      
)

# Pasar la ruta del fichero  al ContadorPalabras.py

salida, error = proceso.communicate(input=ruta_archivo.encode("utf8"))  

# Imprimir salida y errores

print("Salida:")
print(salida.decode('latin1')) 
print("Errores:")
print(error.decode('latin1'))  

# Escribimos la salida
with open(ruta_archivo_temp,'w') as fichero_temp:
    escritor = fichero_temp.write(str(salida))