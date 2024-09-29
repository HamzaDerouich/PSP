#Funciones
def Saludar(a):
    return f"Hola {a}, ¿cómo estás?"

def SumarNumeros(a,b):
    return a + b

nombre = input("Ingrese su nombre:")
print(Saludar(nombre))

try:
    a = int(input("Digite el primer número: "))
    b = int(input("Digit el segundo número: "))
    print("El resultado de la suma es: "+SumarNumeros(a,b))
except ValueError:
         print("Por favor, ingrese un número válido.")

