lista_centro = []

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

def crear_cliente():
    nombre = input("Dime el nombre del cliente: ")
    apellido = input("Dime el apellido del cliente: ")
    while True:
        try:
            telefono = input("Dime el telefono del cliente: ")
            if len((telefono)) == 9 and telefono.isdigit():
                break
            else:
                print("El teléfono debe de tener 9 dígitos")
        except ValueError as err:
            print("Error", err)

    while True:
        try:
            identificador = input("Dime el identificador del cliente (3 números): ")
            if 0 < len((identificador)) < 4 and identificador.isdigit():
                break
            else:
                print("El identificador debe tener 3 dígitos")
        except ValueError as err:
            print("Error", err)

    return nombre, apellido, telefono, identificador


def agregar_cliente():
    nombre, apellido, telefono, identificador = crear_cliente()
    cliente0 = Clientes(nombre, apellido, telefono, identificador)
    lista_centro.append(cliente0)

#Agregar un cliente en la lista del centro. 
# No se podrá agregar si en la misma ya se
# encuentra registrado

def quitar_cliente():
    if not lista_centro:
        print("No hay ningún cliente registrado ahora mismo")
        return
    
    print("\nEsta es la lista de clientes")
    for i, cliente in enumerate(lista_centro):
        print(f"{i + 1} {cliente.nombre} {cliente.apellido}")
    while True:
        try:
            posicion_cliente = int(input("\nDime el número del cliente que quieres quitar: "))
            if 0 < posicion_cliente <= len(lista_centro):
                eliminado = lista_centro.pop(posicion_cliente - 1)
                print(f"\nEl cliente {eliminado.nombre} {eliminado.apellido} fue eliminado con éxito")

                if len(lista_centro) == 0:
                    print("La lista actualmente esta vacía")
                    break

                else:
                    print("\nLa lista actual es:")
                    for i, cliente in enumerate(lista_centro):
                        print(f"{i + 1} {cliente.nombre} {cliente.apellido}")
                    
                    break
            
            else:
                print("Número de cliente invalido. Intente de nuevo")

        except ValueError as err:
            print("Error:", err)




quitar_cliente()

#Quitar un cliente en la lista del centro. 
# No se podrá quitar si el mismo tiene reservas pendientes.

lista_morosos = []
#Listar clientes morosos de una cancha o de la lista de clientes totales