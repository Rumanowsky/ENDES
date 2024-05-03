class Persona:
    def __init__(self, dni, nombre, apellidos, fecha):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos  
        self.fecha = fecha
    def __str__(self):
        return f"{self.dni} - {self.nombre} {self.apellidos} ({self.fecha})"
class Alumno(Persona):
        def __init__(self, dni, nombre, apellidos, fecha, nia):
            super().__init__(dni, nombre, apellidos, fecha)
            self.nia = nia  #numero de identificación de alumno
class Trabajador(Persona):
        def __init__(self, dni, nombre, apellidos, fecha, nrp):
            super().__init__(dni, nombre, apellidos, fecha)
            self.nrp = nrp   #numero de registro patronal

class Profesor(Trabajador):
    def __init__(self, dni, nombre, apellidos, fecha, nrp, dpto):
        super().__init__(dni, nombre, apellidos, fecha, nrp)
        self.dpto = dpto
p1 = Persona("123456W", "Nom1", "apeel1", "14/01/2021")
print(p1)
a1 = Alumno("993456W", "Nom2", "apeel2", "14/01/2022", "DAW")
print(a1)
t1 = Trabajador("19788856W", "Nom3", "apeel3", "01/01/2022", "TRA")
print(t1)
pr1 = Profesor("6688856W", "Nom4", "apeel4", "01/12/2022", "PRO", "INFO")
print(pr1)
