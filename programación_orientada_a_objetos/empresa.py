class empresa:
    def __init__(self,nombre,razon_social,actividad):
        self.nombre = nombre
        self.razon_social = razon_social
        self.actividad = actividad


class empleado:
    def __init__(self,nombre,edad,sueldo_bruto):
        self.nombre = nombre
        self.edad = edad
        self.sueldo_bruto = sueldo_bruto

        def mostrar_datos(self):
            print("Nombre: " + self.nombre)

class directivo:
    def __init__(self,nombre,edad,categoria):
        self.nombre = nombre
        self.edad = edad
        self.categoria = categoria 
        self.subordinados = []
    
    def asignar_subordinado(self, subordinados):
        self.subordinados.append(empleado)
    

class cliente:
    def __init__(self,nombre,edad,telefono):
        self.nombre = nombre 
        self.edad = edad
        self.telefono = telefono


def menu():

    empresas_lista = []
    empleados_lista = []
    clientes_lista = []
    directivos_lista = []

    while True:
        print("1.Añadir Empresa")
        print("2.Añadir Empleado")
        print("3.Añadir Cliente")
        print("4.Añadir Directivo")
        print("5.Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            nombre = input("Dime el nombre: ")
            razon_social = input("Dime la razon_social: ")
            actividad = input("Dime la actividad: ")
            empresa0 = empresa(nombre, razon_social, actividad)
            empresa.append(empresa0)

        elif opcion == 2:
            nombre = input("Dime el nombre: ")
            edad = input("Dime la edad: ")
            sueldo_bruto = input("Dime el sueldo: ")
            empleado0 = empleado(nombre, edad, sueldo_bruto)
            empleado.append(empleado0)

        elif opcion == 3:
            nombre = input("Dime el nombre: ")
            edad = input("Dime la edad: ")
            numero_telefono = input("Dime el numero: ")
            cliente0 = cliente(nombre, edad, numero_telefono)
            cliente.append(cliente0)

        elif opcion == 4:
            lista2_directivos = []
            for directivo in directivos_lista:
                print(directivo)
            eleccion_directivo = input("Dime el directivo: ")
            lista2_directivos.append(eleccion_directivo)
            nombre = input("Dime el nombre: ")
            edad = input("Dime la edad: ")
            categoria = input("Dime la categoría: ")
            sueldo_bruto = input("Dime el sueldo bruto: ")
            directivo0 = directivo(nombre, edad, categoria, sueldo_bruto)
            directivo.append(directivo0)

        elif opcion == 5:
            break

        else:
            print("Introduce un número del 1 al 5")

menu()