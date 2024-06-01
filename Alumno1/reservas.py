lista_reservas = []

class Reserva:
    def __init__(self, numero_reserva, fecha, cliente, cancha):
        self.numero_reserva = numero_reserva
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha

    def __str__(self):
        return f"Reserva {self.numero_reserva}, Fecha: {self.fecha}, Cliente: {self.cliente}, Cancha: {self.cancha}"

def crear_reserva(lista_clientes, lista_canchas):
    numero_reserva = int(input("Dime el número de la reserva: "))
    fecha = input("Dime la fecha de la reserva (Día/Mes/Año): ")

    cliente_id = input("Dime el identificador del cliente: ")
    cliente = None
    for cliente_id in lista_clientes:
        if cliente_id.identificador == cliente_id:
            cliente = cliente_id
            break

    if cliente is None or not cliente.activo or cliente.saldo < -2000:
        print("Cliente no existe, no activo o con saldo negativo mayor a -2000.")
        return

    cancha_num = input("Dime el número de la cancha: ")
    cancha = None
    for cancha_id in lista_canchas:
        if cancha_id.numero == int(cancha_num):
            cancha = cancha_id
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

def listar_reservas_cancha():
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

def listar_reservas_cliente():
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

def mostrar_saldo_cliente(lista_clientes):
    cliente_id = input("Dime el identificador del cliente: ")
    cliente = None
    for cliente_item in lista_clientes:
        if cliente_item.identificador == cliente_id:
            cliente = cliente_item
            break

    if cliente:
        print(f"Saldo del cliente: {cliente.saldo}")
    else:
        print("Cliente no encontrado.")

def registrar_pago(lista_clientes):
    cliente_id = input("Dime el identificador del cliente: ")
    cliente = None
    for cliente_item in lista_clientes:
        if cliente_item.identificador == cliente_id:
            cliente = cliente_item
            break

    if cliente:
        pago = float(input(f"Dime el pago: "))
        cliente.saldo += pago
        print(f"Nuevo saldo del cliente: ")
    else:
        print("Cliente no encontrado.")
