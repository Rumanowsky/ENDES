peliculas = []
salas = []
sesiones = []

class Pelicula:
    def _init_(self, titulo, duracion, clasf_edad, director):
        self.titulo = titulo
        self.duracion = duracion
        self.clasf_edad = clasf_edad
        self.director = director

    def info_peliculas(self):
        return (f"Estos son los datos:", self.titulo, self.duracion, self.clasf_edad, self.director)

class Sala:
    def _init_(self, numero, capacidad, tipo_proyeccion):
        self.numero = numero
        self.capacidad = capacidad
        self.tipo_proyeccion = tipo_proyeccion #preguntar
        self.asientos_disponibles = capacidad

    @property
    def verificar_disponibilidad(self):
        return self.asientos_disponibles > 0
    
    @property
    def tipo_proyeccion(self):
        return self.tipo_proyeccion
    
    @tipo_proyeccion.setter
    def tipo_proyeccion(self, tipo):
        if tipo not in ("2D", "3D"):
            print("El tipo no es correcto")
        else:
            self.tipo_proyeccion = tipo

#creas una variable que instancia un obj tipo sala
#sala.append
#mi_sala = sala("1", "3D", "2D")
class Sesion:
    def _init_(self, pelicula, hora, sala):
        self.pelicula = pelicula
        self.hora = hora
        self.sala = sala

    def asignar_pelicula(self, pelicula):
        self.pelicula = pelicula

    def asignar_sala(self, sala):
        self.sala = sala
    
    def mostrar_info_sesion(self):
        return "{self.pelicula.mostrar_info()} -sala {self.sala.numero}"
    


class Entrada: 
    def _init_(self, asiento, precio, sesion):
        self.asiento = asiento
        self.precio = precio 
        self.sesion = sesion

def menu():
    while True:
        print("1.Añadir Película")
        print("2.Añadir Sala")
        print("3.Añadir Sesión")
        print("4.Mostrar programación")
        print("5.Vender entrada")

        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            titulo_o = input("Dime el título: ")
            duracion_o = input("Dime la duración: ")
            clasificacion_o = input("Dime la clasificación de edad: ")
            director_o = input("Dime el director: ")
            pelicula1 = Pelicula(titulo_o, duracion_o, clasificacion_o, director_o)
            peliculas.append(pelicula1)

        elif opcion == 2:
            numero_o = input("Dime el número de la sala: ")
            capacidad_o = input("Dime la capacidad de la sala: ")
            tipo_proyeccion_o = input("Dime el tipo de proyeccion")
        
        elif opcion == 3:
            for i in peliculas:
                print(i.titulo)

        
        elif opcion == 4:
            hola = 1

            #numero, capacidad, tipo_proyeccion


menu()

