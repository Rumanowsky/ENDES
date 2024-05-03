class cuenta_bancaria:
    def __init__(self,saldo = 0):
        self.saldo = saldo

    def depositar_dinero(self):
        self.saldo + int(input("Introduce el saldo que quieras depositar: "))
    
    def retirar_dinero(self):
        self.saldo - int(input("Introduce el salto que quieres retirar: "))

    def mostrar_saldo(self):
        return self.saldo

saldo1 = cuenta_bancaria (500)

saldo1.retirar_dinero()
print(saldo1.mostrar_saldo())

