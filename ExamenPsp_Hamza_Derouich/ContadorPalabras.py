#Función que cuenta el número de palabras que existen en un fichero

def ContadorPalabrasFichero(palabra):
    contador_palabra = 0
    fichero = open(ruta)
    c = 0
    while  c != "" :
        c = fichero.read(1)
        contador_palabra +=1
    return contador_palabra

# Función que pide los datos al usario
def PedirDatos():
    try:
        ruta = str(input(r""))
        return ruta
    except ValueError:
        print("Por favor, ingrese un dato valido!!.")


# Llamada a las funciones 

#ruta = r"C:\Users\dam23\Desktop\Fichero.txt" -> ruta utilizada
ruta = PedirDatos()
nPalabra = ContadorPalabrasFichero(ruta)    
print(str(nPalabra))