class Objeto :
    def __init__(self, dato1, dato2):
        self.dato1 = dato1
        self.dato2 = dato2
    def calcular_media(self):

        return (self.dato1 + self.dato2) / 2 
    
p = Objeto(3, 4)
# Accedemos al método. Necesitamos paréntesis
print(p.calcular_media())
