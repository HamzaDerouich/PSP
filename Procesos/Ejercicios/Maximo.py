# Ejercico sacar el maximo de una lista de números
def PedirNumeros():
    lista_numeros = []
    i = 0
    print("Para finalizar, digite 0")
    while True:
        try:
         numero = int(input("Ingrese el número: "))
         if numero != 0:
            lista_numeros.append(numero)
         else:
             break;   
        except Exception:
            print("Número no valido!!")
    return lista_numeros
            
def SacarMaximo(lista_numeros):
    max = lista_numeros[0]
    for j in lista_numeros:
        if max < j + 1:
            max = j
        else:
            j = max     
    return max       
        
lista_numeros = PedirNumeros()
max = SacarMaximo(lista_numeros)
print(f"El maximo de la lista de numeros {lista_numeros}  -> {max} ")       
