class Arbol:
    def __init__(self):
        self.tipo = ""
        self.edad = 0
        self.lugar_plantado = ""
        self.raiz = Raiz()
        self.tronco = Tronco()
        self.copa = Copa()

class Tronco:
    def __init__(self):
        self.altura = 0
        self.diamentro = 0

class Raiz:
     def __init__(self):
        self.numero_raices = 0
        self.tamanio_medio = 0.0

class copa:
    def __init__(self):
        
