from enum import Enum

class Inmueble:
    def __init__(self, identificador: int, area: int, direccion: str):
        self.identificador = identificador
        self.area = area
        self.direccion = direccion
        self.precio_venta = 0.0
    
    def calcular_precio_venta(self, valor_area: float):
        self.precio_venta = self.area * valor_area
        return self.precio_venta
    
    def imprimir(self):
        print(f"Identificador inmobiliario: {self.identificador}")
        print(f"Área: {self.area} m²")
        print(f"Dirección: {self.direccion}")
        print(f"Precio de venta: ${self.precio_venta:,.2f}")


class InmuebleVivienda(Inmueble):
    def __init__(self, identificador: int, area: int, direccion: str, 
                 num_habitaciones: int, num_banos: int):
        super().__init__(identificador, area, direccion)
        self.num_habitaciones = num_habitaciones
        self.num_banos = num_banos
    
    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones: {self.num_habitaciones}")
        print(f"Número de baños: {self.num_banos}")


class Casa(InmuebleVivienda):
    def __init__(self, identificador: int, area: int, direccion: str, 
                 num_habitaciones: int, num_banos: int, num_pisos: int):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos)
        self.num_pisos = num_pisos
    
    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos: {self.num_pisos}")


class CasaRural(Casa):
    valor_area = 1500000
    
    def __init__(self, identificador: int, area: int, direccion: str, 
                 num_habitaciones: int, num_banos: int, num_pisos: int,
                 distancia_cabecera: int, altitud: int):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud
    
    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal: {self.distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar: {self.altitud} metros")
        print()


class CasaUrbana(Casa):
    def __init__(self, identificador: int, area: int, direccion: str, 
                 num_habitaciones: int, num_banos: int, num_pisos: int):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos, num_pisos)


class CasaConjuntoCerrado(CasaUrbana):
    valor_area = 2500000
    
    def __init__(self, identificador: int, area: int, direccion: str, 
                 num_habitaciones: int, num_banos: int, num_pisos: int,
                 valor_administracion: float, tiene_piscina: bool, tiene_campos: bool):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos, num_pisos)
        self.valor_administracion = valor_administracion
        self.tiene_piscina = tiene_piscina
        self.tiene_campos = tiene_campos
    
    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración: ${self.valor_administracion:,.2f}")
        print(f"Tiene piscina: {'Sí' if self.tiene_piscina else 'No'}")
        print(f"Tiene campos deportivos: {'Sí' if self.tiene_campos else 'No'}")
        print()


class CasaIndependiente(CasaUrbana):
    valor_area = 3000000
    
    def __init__(self, identificador: int, area: int, direccion: str, 
                 num_habitaciones: int, num_banos: int, num_pisos: int):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos, num_pisos)
    
    def imprimir(self):
        super().imprimir()
        print()


class Apartamento(InmuebleVivienda):
    def __init__(self, identificador: int, area: int, direccion: str, 
                 num_habitaciones: int, num_banos: int):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos)


class ApartamentoFamiliar(Apartamento):
    valor_area = 2000000
    
    def __init__(self, identificador: int, area: int, direccion: str, 
                 num_habitaciones: int, num_banos: int, valor_administracion: float):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos)
        self.valor_administracion = valor_administracion
    
    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración: ${self.valor_administracion:,.2f}")
        print()


class Apartaestudio(Apartamento):
    valor_area = 1500000
    
    def __init__(self, identificador: int, area: int, direccion: str):
        super().__init__(identificador, area, direccion, 1, 1)
    
    def imprimir(self):
        super().imprimir()
        print()


class Local(Inmueble):
    class Tipo(Enum):
        INTERNO = 1
        CALLE = 2
    
    def __init__(self, identificador: int, area: int, direccion: str, tipo_local: 'Local.Tipo'):
        super().__init__(identificador, area, direccion)
        self.tipo_local = tipo_local
    
    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {self.tipo_local.name}")


class LocalComercial(Local):
    valor_area = 3000000
    
    def __init__(self, identificador: int, area: int, direccion: str, 
                 tipo_local: 'Local.Tipo', centro_comercial: str):
        super().__init__(identificador, area, direccion, tipo_local)
        self.centro_comercial = centro_comercial
    
    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial: {self.centro_comercial}")
        print()


class Oficina(Local):
    valor_area = 3500000
    
    def __init__(self, identificador: int, area: int, direccion: str, 
                 tipo_local: 'Local.Tipo', es_gobierno: bool):
        super().__init__(identificador, area, direccion, tipo_local)
        self.es_gobierno = es_gobierno
    
    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental: {'Sí' if self.es_gobierno else 'No'}")
        print()


def main():
    # Ejemplo 1: ApartamentoFamiliar (exactamente como en el ejercicio original)
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    print("Datos apartamento")
    apto1.calcular_precio_venta(apto1.valor_area)
    apto1.imprimir()

    # Ejemplo 2: Apartaestudio (exactamente como en el ejercicio original)
    print("Datos apartamento")
    aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
    aptestudio1.calcular_precio_venta(aptestudio1.valor_area)
    aptestudio1.imprimir()

    # Ejemplo adicional (no en el original) para mostrar otro tipo
    print("\nEjemplo adicional con CasaConjuntoCerrado:")
    casa_cerrado = CasaConjuntoCerrado(
        identificador=456789,
        area=180,
        direccion="Calle 100 #15-20",
        num_habitaciones=4,
        num_banos=3,
        num_pisos=2,
        valor_administracion=350000,
        tiene_piscina=True,
        tiene_campos=True
    )
    casa_cerrado.calcular_precio_venta(casa_cerrado.valor_area)
    casa_cerrado.imprimir()


if __name__ == "__main__":
    main()
