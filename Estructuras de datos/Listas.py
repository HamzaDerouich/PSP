# Listas
datos = [] # A si se declara los datos a la lista 
datos = ["1", "2", "3", "4", "5","2"] # Llenamos la lista de datos

# Métodos de las listas

datos_invertidos = datos[::-1] #Invertir Cadenas
print(datos_invertidos)

# Agrega un elemento al final de la lista 
datos.append("Messi")
print(datos)

# Agremamos más datos a una lista o otra lista
datos.extend(["Hamza","20","Pera"])
print(datos)

# Insertamos un datos en posición especifica 
datos.insert(1,"Paxo")
print(datos)

#Elimina la primera aparicion del  elemento en la lista
datos.remove("2")
print(datos)

#Elimnia el último elemento de la lista , si se le proporciona un indice al elimina los dos 
datos.pop()
print(datos)

# Devuelve el índice de la primera aparición de un valor en la lista. Puedes especificar un rango opcional con parámetros start y end.
numeros =  [1,2,3,4,5,6]
aparece = numeros.count(1)
print(f"Las veces que aparece son: {aparece} ")


#Ordenamos el array de forma descdendente o ascendente
numeros.sort( reverse= True )
print(numeros)

# También tenemos los metodos suma max min y len

