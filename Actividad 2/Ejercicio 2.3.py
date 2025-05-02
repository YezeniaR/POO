from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class TipoAutomovil(Enum):
    CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, 
                 num_puertas, num_asientos, velocidad_max, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.velocidad_max = velocidad_max
        self.color = color
        self.velocidad_actual = 0

    # Métodos get
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_tipo_combustible(self):
        return self.tipo_combustible

    def get_tipo_automovil(self):
        return self.tipo_automovil

    def get_num_puertas(self):
        return self.num_puertas

    def get_num_asientos(self):
        return self.num_asientos

    def get_velocidad_max(self):
        return self.velocidad_max

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    # Métodos set
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_tipo_combustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def set_num_puertas(self, num_puertas):
        self.num_puertas = num_puertas

    def set_num_asientos(self, num_asientos):
        self.num_asientos = num_asientos

    def set_velocidad_max(self, velocidad_max):
        self.velocidad_max = velocidad_max

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    # Métodos de operación
    def acelerar(self, incremento):
        nueva_velocidad = self.velocidad_actual + incremento
        if nueva_velocidad <= self.velocidad_max:
            self.velocidad_actual = nueva_velocidad
        else:
            print("No se puede superar la velocidad máxima del vehículo")

    def desacelerar(self, decremento):
        nueva_velocidad = self.velocidad_actual - decremento
        if nueva_velocidad >= 0:
            self.velocidad_actual = nueva_velocidad
        else:
            print("No se puede tener una velocidad negativa")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual > 0:
            return distancia / self.velocidad_actual
        else:
            return 0

    def imprimir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor}L")
        print(f"Tipo combustible: {self.tipo_combustible.value}")
        print(f"Tipo automóvil: {self.tipo_automovil.value}")
        print(f"Número de puertas: {self.num_puertas}")
        print(f"Asientos: {self.num_asientos}")
        print(f"Velocidad máxima: {self.velocidad_max} km/h")
        print(f"Color: {self.color.value}")


def main():
    # Crear un automóvil
    auto = Automovil(
        marca="Ford",
        modelo=2018,
        motor=3,
        tipo_combustible=TipoCombustible.DIESEL,
        tipo_automovil=TipoAutomovil.EJECUTIVO,
        num_puertas=5,
        num_asientos=6,
        velocidad_max=250,
        color=Color.NEGRO
    )

    # Probar funcionalidades
    auto.imprimir()
    print("\nProbando operaciones de velocidad:")
    
    auto.set_velocidad_actual(100)
    print(f"Velocidad actual: {auto.get_velocidad_actual()} km/h")
    
    auto.acelerar(20)
    print(f"Después de acelerar 20 km/h: {auto.get_velocidad_actual()} km/h")
    
    auto.desacelerar(50)
    print(f"Después de desacelerar 50 km/h: {auto.get_velocidad_actual()} km/h")
    
    auto.frenar()
    print(f"Después de frenar: {auto.get_velocidad_actual()} km/h")
    
    # Intentar desacelerar más allá de 0
    auto.desacelerar(20)

if __name__ == "__main__":
    main()
