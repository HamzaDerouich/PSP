class Banco:
    def __init__(self, nombre, direccion, telefono,saldo):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.saldo = saldo

    def  retirarDinero(self, cantidad):
        self.saldo = self.saldo - cantidad
        return self.saldo

    def  depositarDinero(self, cantidad):
        self.saldo = self.saldo + cantidad
        return self.saldo

    def  consultaSaldo(self):
        return self.saldo

    def  consultaNombre(self):
        return self.nombre

    def  consultaDireccion(self):
        return self.direccion

    def  consultaTelefono(self):
        return self.telefono