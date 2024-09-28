def RealizarOperacion(operacion, a, b):
    try:
        if operacion == 1:
            return a + b
        elif operacion == 2:
            return a - b
        elif operacion == 3:
            return a * b
        elif operacion == 4:
            if b == 0:
                return "Error: División por cero no permitida"
            return a / b
        elif operacion == 5:
            if b == 0:
                return "Error: Módulo por cero no permitido"
            return a % b
    except Exception as e:
        return f"Se produjo un error: {e}"

salir = 0
while salir != 6:
    print(
        "Digite la operación que deseas realizar:" +
        "\n 1. Suma" +
        "\n 2. Resta" +
        "\n 3. Multiplicación" +
        "\n 4. División" +
        "\n 5. Módulo" +
        "\n 6. Salir"
    )

    try:
        operacion = int(input("Digite el número de la operación: "))
        if operacion == 6:
            print("Saliendo...")
            break
        elif 1 <= operacion <= 5:
            a = int(input("Digite el primer número: "))
            b = int(input("Digite el segundo número: "))
            print(f"El resultado de la operación = {RealizarOperacion(operacion, a, b)}")
        else:
            print("Operación no válida, por favor ingrese un número entre 1 y 6.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

