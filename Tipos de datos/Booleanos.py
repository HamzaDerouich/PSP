# Valores boolean 
mayorEdad = False
edad = int((input("Digite tu edad: ")))
if edad >= 18: mayorEdad = True
else: mayorEdad = False
if not mayorEdad: print("No eres mayor de edad!!")
else: print("Eres mayor de edad!!")