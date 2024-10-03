def SucesionFibonacci():
    numero = int(input("Ingrese el número: "))
    i = 0
    a = 0
    b = 1
    suma = 0
    while i < numero:
        print(f"\n{a}")
        suma = a + b
        a = b
        b = suma
        i += 1


SucesionFibonacci()
