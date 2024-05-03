class Persona:
    def __init__(self, nombre, edad = None):
        self.nombre = nombre # definimos las propiedades
        self.edad = edad
#definimos los métodos de la clase
    def es_mayor_de_edad(self): 
        return self.edad >= 18
    def imprimir(self):
        return self.nombre

class Clase:
    def __init__(self, nombre, docente: Persona):
        self.nombre = nombre 
        self.docente = docente
        self.alumnos = []

#Docente: simple // unos_alumnos: compuesto
def modifica_datos(un_docente, unos_alumnos):
    un_docente = "Sergio"
    unos_alumnos.append ("Oscar")

mi_clase = Clase("DAW1", Persona("Encarna"))
mi_clase.alumnos.append("Pablo")
mi_clase.alumnos.append("Maria")

#¿Qué pasa al pasar un tipo simple y uno compuesto por parámetro?
modifica_datos(mi_clase.docente, mi_clase.alumnos)

print("El docente de la clase es:", mi_clase.docente.nombre)
print("La clase tiene {} alumnos".format(str(len(mi_clase.alumnos))))
