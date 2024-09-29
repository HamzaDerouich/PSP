import random
letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letras_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras_mayusculas_minusculas = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'  ]
letras_mayusculas_minusculas_numeros =  [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'  ]
letras_mayusculas_minusculas_numeros =  [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'  ]
letras_mayusculas_minusculas_numeros_caracteres =  [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?'  ]
caracteres_especiales = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '/', '?']


def GenaradorContraseñasSimples(array, longitud):
        resultado = ""
        i =  0
        while( i < longitud ):
             resultado += array[random.randint(0,len(array)-1)]
             i += 1
        return resultado
    
def GenaradorContraseñasCompuestasMayusculasMinusculas(longitud):  
        resultado = "".join(random.choice(letras_mayusculas_minusculas) for i in range(longitud))
        return resultado  

def GenaradorContraseñasCompuestasMayusculasMinusculasNumeros(longitud):  
        resultado = "".join(random.choice(letras_mayusculas_minusculas_numeros) for i in range(longitud))
        return resultado  
def GenaradorContraseñasCompuestasMayusculasMinusculasNumerosCaracteres(longitud):  
        resultado = "".join(random.choice(letras_mayusculas_minusculas_numeros_caracteres) for i in range(longitud))
        return resultado  



def OpcionesContraseñas(longitud, tipo):
    if tipo == 1:
        resultado = GenaradorContraseñasSimples(letras_mayusculas,longitud)
        print(f"Contraseña generada = {resultado}")  
    elif tipo == 2:
        resultado = GenaradorContraseñasSimples(letras_minusculas,longitud)
        print(f"Contraseña generada = {resultado}")
    elif tipo == 3:
         resultado = GenaradorContraseñasSimples(numeros,longitud)
         print(f"Contraseña generada = {resultado}")
    elif tipo == 4:
         resultado = GenaradorContraseñasSimples(caracteres_especiales,longitud)
         print(f"Contraseña generada = {resultado}")         
    elif tipo ==5:
        resultado = GenaradorContraseñasCompuestasMayusculasMinusculas(longitud)
        print(f"Contraseña generada = {resultado}")
    elif tipo == 6:
        resultado =   resultado = GenaradorContraseñasCompuestasMayusculasMinusculasNumeros(longitud)
        print(f"Contraseña generada = {resultado}")  
    elif tipo == 7:
        resultado =   resultado = GenaradorContraseñasCompuestasMayusculasMinusculasNumerosCaracteres(longitud)
        print(f"Contraseña generada = {resultado}")  
           
         
    

def GeneradorContraseñasApp():
    try:
        longitud = int(input("Digite la longitud de la contraseña: "))
        tipo_contraseña = int(input(
            "\tCaracteres usados: "
            "\n1.Letras Mayusculas: "+
            "\n2.Letras Minusculas: "+
            "\n3.Números: "+
            "\n4.Carcteres especiales"
            "\n\t_______COMBINACIONES______ "
            "\n5.Letras Mayusculas + Minusculas: "+
            "\n6.Letras Mayusculas + Minusculas + Números: "+
            "\n7.Letras Mayusculas + Minusculas + Números + Caracteres Especiales: "
            ))
        OpcionesContraseñas(longitud , tipo_contraseña)
    except ValueError:
        print("Por favor, ingrese un número válido.")

GeneradorContraseñasApp()