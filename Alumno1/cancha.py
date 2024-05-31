lista_canchas = []

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

def crear_cancha():
    while True:
        numero = input("Dime el número de la cancha: ")
        if numero.isdigit():
            numero = int(numero)
            break
        else:
            print("El número de la cancha debe ser numérico")

    deporte = input("Dime el deporte de la cancha: ")
    
    precio = input("Dime el precio de la cancha: ")

    return numero, deporte, precio

def agregar_cancha():
    numero, deporte, precio = crear_cancha()
    for cancha in lista_canchas:
        if cancha.numero == numero:
            print("Cancha ya registrada")
            return
    cancha0 = Cancha(numero, deporte, precio)
    lista_canchas.append(cancha0)
    print(f"Cancha {numero} de {deporte} añadida con éxito")

def listar_canchas():
    deporte = input("Dime el deporte: ")
    canchas_deporte = []
    for cancha in lista_canchas:
        if cancha.deporte == deporte:
            canchas_deporte.append(cancha)
    
    if canchas_deporte:
        print(f"\nCanchas de {deporte}:")
        for cancha in canchas_deporte:
            print(cancha)
    else:
        print(f"No hay canchas registradas para el deporte {deporte}")


def quitar_cancha():
    if not lista_canchas:
        print("No hay ninguna cancha registrada ahora mismo.")
        return

    print("\nEsta es la lista de canchas:")
    for i, cancha in enumerate(lista_canchas):
        print(f"{i + 1}. {cancha}")

    while True:
        try:
            posicion_cancha = int(input("\nDime el número de la cancha que quieres quitar: "))
            if 0 < posicion_cancha <= len(lista_canchas):
                cancha_a_quitar = lista_canchas[posicion_cancha - 1]
                if cancha_a_quitar.reservas:
                    print(f"No se puede quitar la cancha {cancha_a_quitar.numero} porque tiene reservas pendientes.")
                    return
                eliminado = lista_canchas.pop(posicion_cancha - 1)
                print(f"\nLa cancha {eliminado.numero} de {eliminado.deporte} fue eliminada con éxito.")
                break
            else:
                print("Número de cancha inválido. Intente de nuevo.")
        except ValueError as err:
            print("Error:", err)