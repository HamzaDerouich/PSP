# Funciones
def Saludar(a):
    return f"Hola {a}, ¿cómo estás?"


def SumarNumeros():
    try:
        a = int(input("Digite el primer número: "))
        b = int(input("Digit el segundo número: "))
        resultado = a + b
        print(f"El resultado de la suma {a} + {b} = {resultado}")
    except ValueError:
        print("Por favor, ingrese un número válido.")


def numerosX(*numeros):  # Puede recibir NªArgumentos
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


def mostrarProducto(**producto):  # Recibe los argumentos como un constructor
    print(producto)


def mostrarProductoDos(**producto):  # Recibe los argumentos como un constructor
    print(
        "Id:" + producto["id"],
        "Nombre:" + producto["nombre"] + "tipo" + producto["tipo"],
    )


print(f"El resultado de la suma de los número es:")
numerosX(2, 4, 5, 67, 7)
nombre = input("Ingrese su nombre:")
print(Saludar(nombre))
SumarNumeros()
mostrarProducto(id="23", nombre="Manzana", tipo="fruta")
mostrarProductoDos(id="23", nombre="Manzana", tipo="fruta")
