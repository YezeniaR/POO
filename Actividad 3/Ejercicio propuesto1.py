from enum import Enum

class Mascota:
    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def __str__(self):
        return f"{self.nombre} ({self.__class__.__name__}), {self.edad} años, color: {self.color}"


class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde
    
    @staticmethod
    def sonido():
        print("Los perros ladran")


class Gato(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto
    
    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")


# Razas de perros pequeños
class Caniche(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class YorkshireTerrier(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Schnauzer(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Chihuahua(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)


# Razas de perros medianos
class Collie(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Dalmata(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Bulldog(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Galgo(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Sabueso(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)


# Razas de perros grandes
class PastorAleman(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Doberman(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Rottweiler(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)


# Tipos de gatos
class GatoSinPelo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class GatoPeloLargo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class GatoPeloCorto(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)


# Razas de gatos sin pelo
class Esfinge(GatoSinPelo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Elfo(GatoSinPelo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Donskoy(GatoSinPelo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)


# Razas de gatos de pelo largo
class Angora(GatoPeloLargo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Himalayo(GatoPeloLargo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Balines(GatoPeloLargo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Somali(GatoPeloLargo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)


# Razas de gatos de pelo corto
class AzulRuso(GatoPeloCorto):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Britanico(GatoPeloCorto):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Manx(GatoPeloCorto):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class DevonRex(GatoPeloCorto):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

def ejecutar_casos_prueba():
    print("\n1. Prueba de sonidos característicos:")
    Perro.sonido()  # Debe imprimir "Los perros ladran"
    Gato.sonido()   # Debe imprimir "Los gatos maúllan y ronronean"
    
    print("\n3. Perros pequeños:")
    caniche = Caniche("Firulais", 2, "blanco", 4.5, False)
    yorkie = YorkshireTerrier("Max", 1, "marrón", 3.2, True)
    print(caniche)
    print(f"¿{yorkie.nombre} muerde? {'Sí' if yorkie.muerde else 'No'}")

    print("\n6. Gatos sin pelo:")
    esfinge = Esfinge("Cleo", 1, "rosado", 1.2, 1.5)
    donskoy = Donskoy("Boris", 2, "gris", 1.0, 1.3)
    print(esfinge)
    print(f"Altura de salto de {donskoy.nombre}: {donskoy.altura_salto} m")

if __name__ == "__main__":
    ejecutar_casos_prueba()
