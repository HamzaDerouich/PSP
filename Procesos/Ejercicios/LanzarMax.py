import subprocess

# Cambia la ruta si es necesario
ruta_maximo = r"C:\Users\dam23\Desktop\PSP\Procesos\Ejercicios\Maximo.py"

# Lanzar proceso
proceso = subprocess.Popen(
    ["python", ruta_maximo],  # Especificar el archivo a ejecutar
    stdout=subprocess.PIPE,    # Capturar la salida estándar
    stdin=subprocess.PIPE,
    stderr=subprocess.PIPE      # Capturar errores si los hay
)

# Pasar la entrada como bytes y esperar a que termine el proceso
salida, errores = proceso.communicate(b"1\n2\n4\n5\n0\n")  # Estos son los números que se simulan como entrada

# Imprimir salida y errores
print("Salida:")
print(salida.decode('latin1'))  # Decodificar la salida a texto
#print("Errores:")
# print(errores.decode())  # Decodificar cualquier error
