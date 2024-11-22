def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Opción 4")
    print("5. Opción 5")
    print("6. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        print("Has seleccionado la Opción 1")
        # Lógica para la Opción 1
    elif opcion == 2:
        print("Has seleccionado la Opción 2")
        # Lógica para la Opción 2
    elif opcion == 3:
        print("Has seleccionado la Opción 3")
        # Lógica para la Opción 3
    elif opcion == 4:
        print("Has seleccionado la Opción 4")
        # Lógica para la Opción 4
    elif opcion == 5:
        print("Has seleccionado la Opción 5")
        # Lógica para la Opción 5
    elif opcion == 6:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 6.")

def menu():
    opcion = 0
    while opcion != 6:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción (1-6): "))
            ejecutar_opcion(opcion)
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Ejecutar el menú
menu()
