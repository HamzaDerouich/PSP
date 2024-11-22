import subprocess

"""
     Lanzar proceso con pop y run mediante una ruta:
"""

# Pedimos los datos para los procesos 
busqueda = input("Introduce el término que deseas buscar: ")
mensaje = input("El nombre del fichero: ")
# Búsqueda de marca
url = f"https://www.marca.com/search?q={busqueda}"

# Abrimos el navegador con la URL

subprocess.Popen(["C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe", url])

# Abrimos el navegador con la URL

subprocess.run(["notepad.exe",mensaje])