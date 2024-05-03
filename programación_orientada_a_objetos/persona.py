class persona:
    def __init__(self,dni=None,nombre=None,apellidos=None,edad=None):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def es_mayor_de_edad(self):
        return self.edad >= 18
    

class principal:
    def main(self):
        persona1 = persona()
        persona2 = persona()
        #Aquí van los datos del primer objeto
        persona1.dni = input("Introduce tu DNI: ")
        persona1.nombre = input("Introduce tu nombre: ")
        persona1.apellidos = input("Introduce tus apellidos: ")
        persona1.edad = input("Introduce tu edad: ")
        #Aquí van los datos del sgundo objeto
        persona2.dni = input("Introduce tu DNI: ")
        persona2.nombre = input("Introduce tu nombre: ")
        persona2.apellidos = input("Introduce tus apellidos: ")
        persona2.edad = input("Introduce tu edad: ")
    

principal().main()