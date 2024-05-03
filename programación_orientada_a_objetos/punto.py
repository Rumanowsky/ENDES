class punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

mi_punto = punto(4,5)
print(mi_punto)
    

class principal:
    def main(self):
        punto1 = punto(5,0)
        punto2 = punto(10,10)
        punto3 = punto(-3,7)
        print(f"({punto1}) ({punto2}) ({punto3})")
        

principal().main()