def ContadorPalabras(ruta,palabra):
    contador_palabra = 0
    for i in range(len(ruta)):
        if ruta[i].lower() == palabra or ruta[i].upper() == palabra:
            contador_palabra += 1
    return contador_palabra

def ContadorPalabrasFichero(ruta , palabra):
    contador_palabra = 0
    fichero = open(ruta)
    c = 0
    while  c != "" :
        c = fichero.read(1)
        if c.lower() == palabra or c.upper() == palabra:
            contador_palabra +=1
    return contador_palabra

## Contador palabras cadena
ruta = "Hola mundo"
nPalabra = ContadorPalabras(ruta,"o")        
print(f"Cantidad de palabras repetidas: {nPalabra} ")

#Contador palabras fichero
ruta_dos = str(input(r"Ingrese la ruta del fichero: "))
##ruta_dos = r"C:\Users\dam23\Desktop\Fichero.txt"
nPalabra_dos = ContadorPalabrasFichero(ruta_dos,"f")        
print(f"Cantidad de palabras repetidas: {nPalabra_dos} ")