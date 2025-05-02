from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    def __init__(self, nombre=None, cantidad_satelites=0, masa=0.0, volumen=0.0,
                 diametro=0, distancia_sol=0, tipo=TipoPlaneta.TERRESTRE, observable=False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa  # en kilogramos
        self.volumen = volumen  # en km³
        self.diametro = diametro  # en km
        self.distancia_sol = distancia_sol  # en millones de km
        self.tipo = tipo
        self.observable = observable

    def imprimir(self):
        print(f"Nombre del planeta: {self.nombre}")
        print(f"Cantidad de satélites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km³")
        print(f"Diámetro: {self.diametro} km")
        print(f"Distancia al Sol: {self.distancia_sol} millones de km")
        print(f"Tipo de planeta: {self.tipo.value}")
        print(f"Observable a simple vista: {'Sí' if self.observable else 'No'}")

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen  # kg/km³

    def es_exterior(self):
        # 1 UA = 149.597870 millones de km
        # Cinturón de asteroides está entre 2.1 y 3.4 UA
        limite_exterior = 3.4 * 149.597870  # millones de km
        return self.distancia_sol > limite_exterior

def main():
    # Crear planetas
    tierra = Planeta(
        nombre="Tierra",
        cantidad_satelites=1,
        masa=5.9736e24,
        volumen=1.08321e12,
        diametro=12742,
        distancia_sol=150,
        tipo=TipoPlaneta.TERRESTRE,
        observable=True
    )

    jupiter = Planeta(
        nombre="Júpiter",
        cantidad_satelites=79,
        masa=1.899e27,
        volumen=1.4313e15,
        diametro=139820,
        distancia_sol=750,
        tipo=TipoPlaneta.GASEOSO,
        observable=True
    )

    # Mostrar información

    tierra.imprimir()
    print(f"Densidad: {tierra.calcular_densidad():.2f} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if tierra.es_exterior() else 'No'}")

    print("\n")
    jupiter.imprimir()
    print(f"Densidad: {jupiter.calcular_densidad():.2f} kg/km³")
    print(f"¿Es planeta exterior?: {'Sí' if jupiter.es_exterior() else 'No'}")

if __name__ == "__main__":
    main()
