lista_centro = []
lista_morosos = []
lista_empleados = []

class Personas:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Clientes(Personas):
    def __init__(self, nombre, apellido, telefono, identificador):
        self.telefono = telefono
        self.identificador = identificador
        super().__init__(nombre, apellido)
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Telefono: {self.telefono}, ID: {self.identificador}"

class Empleados(Personas):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.desocupado = True
        self.lista_tareas = []

    def registrar_cancha(self):
        if self.desocupado:
            self.desocupado = False
            print(f"El empleado {self.nombre} {self.apellido} ha sido registrado a la cancha.")
        else:
            print(f"El empleado {self.nombre} {self.apellido} ya está registrado en una cancha.")

    def asignar_tarea(self, tarea):
        self.lista_tareas.append(tarea)
        self.desocupado = False
        print(f"Tarea '{tarea}' asignada a {self.nombre} {self.apellido}")

    def quitar_tarea(self, tarea):
        if tarea in self.lista_tareas:
            self.lista_tareas.remove(tarea)
            print(f"Tarea '{tarea}' quitada de {self.nombre} {self.apellido}")
        else:
            print(f"Tarea '{tarea}' no encontrada en la lista de tareas de {self.nombre} {self.apellido}")

        if not self.lista_tareas:
            self.desocupado = True

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Desocupado: {'Sí' if self.desocupado else 'No'}, Tareas: {', '.join(self.lista_tareas)}"


def crear_cliente():
    nombre = input("Dime el nombre del cliente: ")
    apellido = input("Dime el apellido del cliente: ")
    while True:
        telefono = input("Dime el teléfono del cliente: ")
        if len(telefono) == 9 and telefono.isdigit():
            break
        else:
            print("El teléfono debe de tener 9 dígitos y ser numérico.")

    while True:
        identificador = input("Dime el identificador del cliente (3 números): ")
        if len(identificador) == 3 and identificador.isdigit():
            break
        else:
            print("El identificador debe tener 3 dígitos y ser numérico.")

    return nombre, apellido, telefono, identificador

def agregar_cliente():
    nombre, apellido, telefono, identificador = crear_cliente()
    for cliente in lista_centro:
        if cliente.identificador == identificador:
            print("Cliente ya registrado")
            return
    cliente0 = Clientes(nombre, apellido, telefono, identificador)
    lista_centro.append(cliente0)
    print(f"Cliente {nombre} {apellido} añadido con éxito")

def quitar_cliente():
    if not lista_centro:
        print("No hay ningún cliente registrado ahora mismo.")
        return

    print("\nEsta es la lista de clientes:")
    for i, cliente in enumerate(lista_centro):
        print(f"{i + 1}. {cliente}")

    while True:
        try:
            posicion_cliente = int(input("\nDime el número del cliente que quieres quitar: "))
            if 0 < posicion_cliente <= len(lista_centro):
                eliminado = lista_centro[posicion_cliente - 1]
                if eliminado.identificador in [cliente.identificador for cliente in lista_morosos]:
                    print(f"No se puede quitar al cliente {eliminado.nombre} {eliminado.apellido} porque tiene reservas pendientes.")
                    return
                eliminado = lista_centro.pop(posicion_cliente - 1)
                print(f"\nEl cliente {eliminado.nombre} {eliminado.apellido} fue eliminado con éxito.")
                break
            else:
                print("Número de cliente inválido. Intente de nuevo.")
        except ValueError as err:
            print("Error:", err)

def registrar_empleado():
    nombre = input("Dime el nombre del empleado: ")
    apellido = input("Dime el apellido del empleado: ")
    empleado = Empleados(nombre, apellido)
    lista_empleados.append(empleado)
    print(f"Empleado {nombre} {apellido} registrado con éxito")

def asignar_tarea_empleado():
    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    print("\nLista de empleados:")
    for i, empleado in enumerate(lista_empleados):
        print(f"{i + 1}. {empleado}")

    while True:
        try:
            num_empleado = int(input("\nDime el número del empleado al que deseas asignar una tarea: "))
            if 0 < num_empleado <= len(lista_empleados):
                tarea = input("Dime la tarea a asignar: ")
                lista_empleados[num_empleado - 1].asignar_tarea(tarea)
                break
            else:
                print("Número de empleado inválido. Intente de nuevo.")
        except ValueError as err:
            print("Error:", err)

def quitar_tarea_empleado():
    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    print("\nLista de empleados:")
    for i, empleado in enumerate(lista_empleados):
        print(f"{i + 1}. {empleado}")

    while True:
        try:
            num_empleado = int(input("\nDime el número del empleado al que deseas quitar una tarea: "))
            if 0 < num_empleado <= len(lista_empleados):
                tarea = input("Dime la tarea a quitar: ")
                lista_empleados[num_empleado - 1].quitar_tarea(tarea)
                break
            else:
                print("Número de empleado inválido. Intente de nuevo.")
        except ValueError as err:
            print("Error:", err)

def listar_empleados_desocupados():
    desocupados = [empleado for empleado in lista_empleados if empleado.desocupado]
    if not desocupados:
        print("No hay empleados desocupados.")
    else:
        print("\nEmpleados desocupados:")
        for empleado in desocupados:
            print(empleado)

def quitar_empleado_cancha():
    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    print("\nLista de empleados:")
    for i, empleado in enumerate(lista_empleados):
        print(f"{i + 1}. {empleado}")

    while True:
        try:
            num_empleado = int(input("\nDime el número del empleado que deseas quitar de la cancha: "))
            if 0 < num_empleado <= len(lista_empleados):
                lista_empleados[num_empleado - 1].desocupado = True
                lista_empleados[num_empleado - 1].lista_tareas = []
                print(f"\nEl empleado {lista_empleados[num_empleado - 1].nombre} {lista_empleados[num_empleado - 1].apellido} ahora está desocupado.")
                break
            else:
                print("Número de empleado inválido. Intente de nuevo.")
        except ValueError as err:
            print("Error:", err)