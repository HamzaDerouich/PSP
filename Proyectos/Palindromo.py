# Función que define si es un palíndromo o no
def EsPalindromo(palabra):
    palabra_limpia = palabra.replace(" ", "").lower()
    palabra_invertida = palabra_limpia[::-1]
    if palabra_limpia == palabra_invertida:
        return f"La palabra/frase '{palabra}' es un palíndromo."
    else:
        return f"La palabra/frase '{palabra}' no es un palíndromo."


# print(EsPalindromo("amo la paloma"))


# Funcion que define si una palabra es un palindromo
def ES_PALINDROMO_DOS(palabra):
    palabra_invertida = ""
    for char in palabra:
        palabra_invertida = char + palabra_invertida
    return palabra_invertida


def QuitarEspacio(palabra):
    palabra_sin_espacios = ""
    for char in palabra:
        if char != " ":
            palabra_sin_espacios = char + palabra_sin_espacios
    return palabra_sin_espacios.lower()


def ComprobarPalindromo(palabra):
    palabra_invertida = EsPalindromo(palabra)
    palabra_invertida = QuitarEspacio(palabra)
    palabra = QuitarEspacio(palabra)
    if palabra_invertida == palabra:
        return f"La palabra/frase '{palabra}' es un palíndromo."
    else:
        return f"La palabra/frase '{palabra}' no es un palíndromo."


print(ComprobarPalindromo("Amo la paloma"))
