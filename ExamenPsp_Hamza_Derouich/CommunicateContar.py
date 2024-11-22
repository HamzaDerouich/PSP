import subprocess

# Cambia la ruta si es necesario
ContadorPalabras = r"C:\Users\dam23\Desktop\PSP\ExamenPsp_Hamza_Derouich\ContadorPalabras.py"
ruta_archivo = r"C:\Users\dam23\Desktop\PSP\Procesos\Ejercicios\Fichero.txt"

# Lanzar proceso
proceso = subprocess.Popen(
    ["python", ContadorPalabras],  
    stdout=subprocess.PIPE,    
    stdin=subprocess.PIPE,
    stderr=subprocess.PIPE      
)

# Pasar la ruta del fichero  al ContadorPalabras.py

salida, error = proceso.communicate(input=ruta_archivo.encode())  

# Imprimir salida y errores

print("Salida:")
print(salida.decode('latin1')) 
print("Errores:")
print(error.decode('latin1'))  
