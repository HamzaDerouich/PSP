
# And { (a) = true (b) = true } -> true
# And { (a) = true (b) = false } -> false

# Or { (a) = true (b) = false } -> true
# And { (a) = false (b) = false } -> false


# not niega  

gas = True
encendido = True

mensaje = "encendido" if gas or encendido else "apagado"
print(mensaje)

mensaje = "encendido" if gas and encendido else "apagado"
print(mensaje)

mensaje = "encendido" if not encendido else "apagado"
print(mensaje)


   