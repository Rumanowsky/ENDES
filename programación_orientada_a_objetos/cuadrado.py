class rectangulo:
    def __init__(self,c1=(0,0),c2=(0,0)):
        self.c1 = c1
        self.c2 = c2
    

class mainRectangulo:
    def main():
        r1 = rectangulo(0,0),(5,5)
        r2 = rectangulo(7,9),(2,3)
    
    def perimetro(x,y):
        return pow(x,2) + pow(y,2)

    def area(x,y):
        return x * y

mainRectangulo.main()       
