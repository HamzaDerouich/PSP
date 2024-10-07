import random
def AdivinarNumero():
    try:
        numero_adivinar = random.randint(1,100)
        numero_ingresado = 1
        contador = 0
        print(numero_adivinar)
        while numero_adivinar != numero_ingresado:
            mensaje = "El número es más grande!!" if numero_adivinar < numero_ingresado else "El número es más pequeño!!" 
            numero_ingresado = int(input("Ingrese el número: "))
            if numero_ingresado <= 100 and numero_ingresado >= 1 :
                print(mensaje)
                contador += 1
            else:
                print("Número no valido, excede el rango!!")
                numero_ingresado = int(input("Ingrese el número: "))
                print(mensaje)
            if numero_adivinar == numero_ingresado:
                print(f"Has acertado, número de intentos totales ${contador} ")
                break
    except Exception :
        print("Formato de número no valido!!!")    
        
AdivinarNumero()