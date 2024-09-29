def  NumeroPar_Impar():
    numero = int(input("Ingrese un número: "))
    mensaje = "El número es par " if numero % 2 == 0 else "El número es impar"
    print(mensaje)
    
NumeroPar_Impar()