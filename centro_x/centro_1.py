from abc import ABC, abstractmethod

lista_centro = []
lista_morosos = []
lista_empleados = []
lista_reservas = []
lista_canchas = []
quejas_empleados = {}

class Personas(ABC):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def __str__(self):
        pass

class Clientes(Personas):
    def __init__(self, nombre, apellido, telefono, identificador, saldo=0):
        self.telefono = telefono
        self.identificador = identificador
        self.saldo = saldo
        super().__init__(nombre, apellido)

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Telefono: {self.telefono}, ID: {self.identificador}, Saldo: {self.saldo}"

class Empleados(Personas):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.desocupado = True
        self.lista_tareas = []

    @property
    def desocupado(self):
        return self._desocupado

    @desocupado.setter
    def desocupado(self, estado):
        self._desocupado = estado

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

class Cancha:
    def __init__(self, numero, deporte, precio, habilitada=True):
        self.numero = numero
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = []
        self.empleados = []

    def __str__(self):
        return f"Cancha {self.numero}, Deporte: {self.deporte}, Precio: {self.precio}, Habilitada: {'Sí' if self.habilitada else 'No'}"

    @classmethod
    def crear_cancha(cls):
        while True:
            numero = input("Dime el número de la cancha: ")
            if numero.isdigit():
                numero = int(numero)
                break
            else:
                print("El número de la cancha debe ser numérico")

        deporte = input("Dime el deporte de la cancha: ")
        precio = input("Dime el precio de la cancha: ")

        return cls(numero, deporte, precio)

class Reserva:
    def __init__(self, numero_reserva, fecha, cliente, cancha):
        self.numero_reserva = numero_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha

    def __str__(self):
        return f"Reserva {self.numero_reserva}, Fecha: {self.fecha}, Cliente: {self.cliente}, Cancha: {self.cancha}"

class Centro:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.lista_canchas = []
        self.lista_clientes = []
        self.lista_empleados = []

    def agregar_cliente(self):
        nombre, apellido, telefono, identificador = self.crear_cliente()
        for cliente in self.lista_clientes:
            if cliente.identificador == identificador:
                print("Cliente ya registrado")
                return
        cliente0 = Clientes(nombre, apellido, telefono, identificador)
        self.lista_clientes.append(cliente0)
        print(f"Cliente {nombre} {apellido} añadido con éxito")

    def quitar_cliente(self):
        if not self.lista_clientes:
            print("No hay ningún cliente registrado ahora mismo.")
            return

        print("\nEsta es la lista de clientes:")
        for i, cliente in enumerate(self.lista_clientes):
            print(f"{i + 1}. {cliente}")

        while True:
            try:
                posicion_cliente = int(input("\nDime el número del cliente que quieres quitar: "))
                if 0 < posicion_cliente <= len(self.lista_clientes):
                    eliminado = self.lista_clientes[posicion_cliente - 1]
                    if eliminado.identificador in [cliente.identificador for cliente in lista_morosos]:
                        print(f"No se puede quitar al cliente {eliminado.nombre} {eliminado.apellido} porque tiene reservas pendientes.")
                        return
                    eliminado = self.lista_clientes.pop(posicion_cliente - 1)
                    print(f"\nEl cliente {eliminado.nombre} {eliminado.apellido} fue eliminado con éxito.")
                    break
                else:
                    print("Número de cliente inválido. Intente de nuevo.")
            except ValueError as err:
                print("Error:", err)

    def registrar_empleado(self):
        nombre = input("Dime el nombre del empleado: ")
        apellido = input("Dime el apellido del empleado: ")
        empleado = Empleados(nombre, apellido)
        self.lista_empleados.append(empleado)
        print(f"Empleado {nombre} {apellido} registrado con éxito")

    def asignar_tarea_empleado(self):
        if not self.lista_empleados:
            print("No hay empleados registrados.")
            return

        print("\nLista de empleados:")
        for i, empleado in enumerate(self.lista_empleados):
            print(f"{i + 1}. {empleado}")

        while True:
            try:
                num_empleado = int(input("\nDime el número del empleado al que deseas asignar una tarea: "))
                if 0 < num_empleado <= len(self.lista_empleados):
                    tarea = input("Dime la tarea a asignar: ")
                    self.lista_empleados[num_empleado - 1].asignar_tarea(tarea)
                    break
                else:
                    print("Número de empleado inválido. Intente de nuevo.")
            except ValueError as err:
                print("Error:", err)

    def quitar_tarea_empleado(self):
        if not self.lista_empleados:
            print("No hay empleados registrados.")
            return

        print("\nLista de empleados:")
        for i, empleado in enumerate(self.lista_empleados):
            print(f"{i + 1}. {empleado}")

        while True:
            try:
                num_empleado = int(input("\nDime el número del empleado al que deseas quitar una tarea: "))
                if 0 < num_empleado <= len(self.lista_empleados):
                    tarea = input("Dime la tarea a quitar: ")
                    self.lista_empleados[num_empleado - 1].quitar_tarea(tarea)
                    break
                else:
                    print("Número de empleado inválido. Intente de nuevo.")
            except ValueError as err:
                print("Error:", err)

    def listar_empleados_desocupados(self):
        desocupados = [empleado for empleado in self.lista_empleados if empleado.desocupado]
        if not desocupados:
            print("No hay empleados desocupados.")
        else:
            print("\nEmpleados desocupados:")
            for empleado in desocupados:
                print(empleado)

    def quitar_empleado_cancha(self):
        if not self.lista_empleados:
            print("No hay empleados registrados.")
            return

        print("\nLista de empleados:")
        for i, empleado in enumerate(self.lista_empleados):
            print(f"{i + 1}. {empleado}")

        while True:
            try:
                num_empleado = int(input("\nDime el número del empleado que deseas quitar de la cancha: "))
                if 0 < num_empleado <= len(self.lista_empleados):
                    self.lista_empleados[num_empleado - 1].desocupado = True
                    self.lista_empleados[num_empleado - 1].lista_tareas = []
                    print(f"\nEl empleado {self.lista_empleados[num_empleado - 1].nombre} {self.lista_empleados[num_empleado - 1].apellido} ahora está desocupado.")
                    break
                else:
                    print("Número de empleado inválido. Intente de nuevo.")
            except ValueError as err:
                print("Error:", err)

    def agregar_cancha(self):
        cancha0 = Cancha.crear_cancha()
        for cancha in self.lista_canchas:
            if cancha.numero == cancha0.numero:
                print("Cancha ya registrada")
                return
        self.lista_canchas.append(cancha0)
        print(f"Cancha {cancha0.numero} de {cancha0.deporte} añadida con éxito")

    def listar_canchas(self):
        deporte = input("Dime el deporte: ")
        canchas_deporte = []
        for cancha in self.lista_canchas:
            if cancha.deporte == deporte:
                canchas_deporte.append(cancha)

        if canchas_deporte:
            print(f"\nCanchas de {deporte}:")
            for cancha in canchas_deporte:
                print(cancha)
        else:
            print(f"No hay canchas registradas para el deporte {deporte}")

    def quitar_cancha(self):
        if not self.lista_canchas:
            print("No hay ninguna cancha registrada ahora mismo.")
            return

        print("\nEsta es la lista de canchas:")
        for i, cancha in enumerate(self.lista_canchas):
            print(f"{i + 1}. {cancha}")

        while True:
            try:
                posicion_cancha = int(input("\nDime el número de la cancha que quieres quitar: "))
                if 0 < posicion_cancha <= len(self.lista_canchas):
                    cancha_a_quitar = self.lista_canchas[posicion_cancha - 1]
                    if cancha_a_quitar.reservas:
                        print(f"No se puede quitar la cancha {cancha_a_quitar.numero} porque tiene reservas pendientes.")
                        return
                    eliminado = self.lista_canchas.pop(posicion_cancha - 1)
                    print(f"\nLa cancha {eliminado.numero} de {eliminado.deporte} fue eliminada con éxito.")
                    break
                else:
                    print("Número de cancha inválido. Intente de nuevo.")
            except ValueError as err:
                print("Error:", err)

    def crear_reserva(self):
        numero_reserva = int(input("Dime el número de la reserva: "))
        fecha = input("Dime la fecha de la reserva (Día/Mes/Año): ")

        cliente_id = input("Dime el identificador del cliente: ")
        cliente = None
        for cliente_item in self.lista_clientes:
            if cliente_item.identificador == cliente_id:
                cliente = cliente_item
                break

        if cliente is None or cliente.saldo < -2000:
            print("Cliente no existe o con saldo negativo mayor a -2000.")
            return

        cancha_num = input("Dime el número de la cancha: ")
        cancha = None
        for cancha_item in self.lista_canchas:
            if cancha_item.numero == int(cancha_num):
                cancha = cancha_item
                break

        if cancha is None or not cancha.habilitada:
            print("Cancha no encontrada o no habilitada.")
            return

        for reserva in lista_reservas:
            if reserva.cancha.numero == cancha.numero and reserva.fecha == fecha:
                print("La cancha ya está reservada en ese horario.")
                return

        reserva0 = Reserva(numero_reserva, fecha, cliente, cancha)
        lista_reservas.append(reserva0)
        cliente.saldo -= cancha.precio
        print(f"Reserva {reserva0} creada con éxito.")

    def listar_reservas_cancha(self):
        cancha_num = input("Dime el número de la cancha: ")
        reservas_cancha = []
        for reserva in lista_reservas:
            if reserva.cancha.numero == int(cancha_num):
                reservas_cancha.append(reserva)

        if reservas_cancha:
            print(f"\nReservas de la cancha {cancha_num}:")
            for reserva in reservas_cancha:
                print(reserva)
        else:
            print(f"No hay reservas para la cancha {cancha_num}.")

    def listar_reservas_cliente(self):
        cliente_id = input("Dime el identificador del cliente: ")
        reservas_cliente = []
        for reserva in lista_reservas:
            if reserva.cliente.identificador == cliente_id:
                reservas_cliente.append(reserva)

        if reservas_cliente:
            print(f"\nReservas del cliente {cliente_id}:")
            for reserva in reservas_cliente:
                print(reserva)
        else:
            print(f"No hay reservas para el cliente {cliente_id}.")

    def mostrar_saldo_cliente(self):
        cliente_id = input("Dime el identificador del cliente: ")
        cliente = None
        for cliente_item in self.lista_clientes:
            if cliente_item.identificador == cliente_id:
                cliente = cliente_item
                break

        if cliente:
            print(f"Saldo del cliente: {cliente.saldo}")
        else:
            print("Cliente no encontrado.")

    def registrar_pago(self):
        cliente_id = input("Dime el identificador del cliente: ")
        cliente = None
        for cliente_item in self.lista_clientes:
            if cliente_item.identificador == cliente_id:
                cliente = cliente_item
                break

        if cliente:
            pago = float(input("Dime el pago: "))
            cliente.saldo += pago
            print(f"Nuevo saldo del cliente: {cliente.saldo}")
        else:
            print("Cliente no encontrado.")

    def poner_queja_empleado(self):
        if not self.lista_empleados:
            print("No hay empleados registrados.")
            return

        print("\nLista de empleados:")
        for i, empleado in enumerate(self.lista_empleados):
            print(f"{i + 1}. {empleado}")

        while True:
            try:
                num_empleado = int(input("\nDime el número del empleado al que deseas poner una queja: "))
                if 0 < num_empleado <= len(self.lista_empleados):
                    empleado = self.lista_empleados[num_empleado - 1]
                    if empleado not in quejas_empleados:
                        quejas_empleados[empleado] = 0
                    quejas_empleados[empleado] += 1
                    print(f"Queja registrada para {empleado.nombre} {empleado.apellido}. Total de quejas: {quejas_empleados[empleado]}")
                    if quejas_empleados[empleado] >= 3:
                        self.lista_empleados.remove(empleado)
                        print(f"El empleado {empleado.nombre} {empleado.apellido} ha sido despedido por acumular 3 quejas.")
                    break
                else:
                    print("Número de empleado inválido. Intente de nuevo.")
            except ValueError as err:
                print("Error:", err)

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

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar Canchas")
        print("2. Gestionar Reservas")
        print("3. Gestionar Clientes")
        print("4. Gestionar Empleados")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            menu_canchas()
        elif opcion == '2':
            menu_reservas()
        elif opcion == '3':
            menu_clientes()
        elif opcion == '4':
            menu_empleados()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Introduce un número entre 1 y 5.")

def menu_canchas():
    while True:
        print("\n--- Menú de Canchas ---")
        print("1. Agregar Cancha")
        print("2. Quitar Cancha")
        print("3. Listar Canchas por Deporte")
        print("4. Regresar al Menú Principal")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            centro.agregar_cancha()
        elif opcion == '2':
            centro.quitar_cancha()
        elif opcion == '3':
            centro.listar_canchas()
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

def menu_reservas():
    while True:
        print("\n--- Menú de Reservas ---")
        print("1. Crear Reserva")
        print("2. Listar Reservas por Cancha")
        print("3. Listar Reservas por Cliente")
        print("4. Regresar al Menú Principal")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            centro.crear_reserva()
        elif opcion == '2':
            centro.listar_reservas_cancha()
        elif opcion == '3':
            centro.listar_reservas_cliente()
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

def menu_clientes():
    while True:
        print("\n--- Menú de Clientes ---")
        print("1. Agregar Cliente")
        print("2. Quitar Cliente")
        print("3. Mostrar Saldo de Cliente")
        print("4. Registrar Pago de Cliente")
        print("5. Regresar al Menú Principal")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            centro.agregar_cliente()
        elif opcion == '2':
            centro.quitar_cliente()
        elif opcion == '3':
            centro.mostrar_saldo_cliente()
        elif opcion == '4':
            centro.registrar_pago()
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")

def menu_empleados():
    while True:
        print("\n--- Menú de Empleados ---")
        print("1. Registrar Empleado")
        print("2. Asignar Tarea a Empleado")
        print("3. Quitar Tarea de Empleado")
        print("4. Listar Empleados Desocupados")
        print("5. Poner Queja a Empleado")
        print("6. Regresar al Menú Principal")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            centro.registrar_empleado()
        elif opcion == '2':
            centro.asignar_tarea_empleado()
        elif opcion == '3':
            centro.quitar_tarea_empleado()
        elif opcion == '4':
            centro.listar_empleados_desocupados()
        elif opcion == '5':
            centro.poner_queja_empleado()
        elif opcion == '6':
            break
        else:
            print("Opción no válida.")

centro = Centro("Centro Rubber y María", "Calle Python 01")

menu_principal()
