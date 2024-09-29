def FactorialNumero():
    resultado = 0
    numero = int(input("Digite el número: "))
    if numero < 0:
        print("No se puede realizar el factor de un número negativo")
    else:
        for i in range(numero - 1, -1, -1):
            if i != 0:
                resultado = numero * i
                numero = resultado
                print(f"!5 = {numero} * {i} = {resultado} ")
    print(f"El resultado de factorizar el número 5 es: {resultado}")


FactorialNumero()
