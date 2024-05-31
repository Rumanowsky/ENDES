lista_centro = []
lista_morosos = []

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

#Agregar un cliente en la lista del centro. 
# No se podrá agregar si en la misma ya se
# encuentra registrado

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


quitar_cliente()

#Quitar un cliente en la lista del centro. 
# No se podrá quitar si el mismo tiene reservas pendientes.

