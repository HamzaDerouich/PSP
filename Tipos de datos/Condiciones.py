"""Introducción a python"""
# if - else - elif
edad = int(input("Digite tu edad:"))
#if edad < 18: print("Eres menor de edad")
#elif edad >= 18 and edad <= 35: print("Te encuentras en el rando de los adultos y jovenes")
#elif edad >35 and edad <= 64: print("Eres una persona adulta")
#elif edad > 65: print("Te vas a morir pronto jejej, es broma eres viejo")

# switch no existe en python -> similar una funcion que lo haga 
def mostrarEdad(e):
    if edad < 18: 
        return 'Eres una persona joven'
    if edad >= 18 and edad <= 35: 
        return "Te encuentras entre lo joven y lo mayor "
    if edad >35 and edad <= 64: 
        return "Eres una persona adulta"
    if edad > 65: 
       return "Te vas a morir pronto jejej, es broma eres viej"

print(mostrarEdad(edad))

