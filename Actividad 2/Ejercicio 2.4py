import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()
    
    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)
    
    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        lados = [self.base, self.altura, hipotenusa]
        lados_redondeados = [round(lado, 6) for lado in lados]
        
        if len(set(lados_redondeados)) == 1:
            print("Es un triángulo equilátero")
        elif len(set(lados_redondeados)) == 2:
            print("Es un triángulo isósceles")
        else:
            print("Es un triángulo escaleno")

def main():
    circulo = Circulo(2)
    rectangulo = Rectangulo(1, 2)
    cuadrado = Cuadrado(3)
    triangulo = TrianguloRectangulo(3, 5)
    
    print("El área del círculo es =", circulo.calcular_area())
    print("El perímetro del círculo es =", circulo.calcular_perimetro())
    print()
    
    print("El área del rectángulo es =", rectangulo.calcular_area())
    print("El perímetro del rectángulo es =", rectangulo.calcular_perimetro())
    print()
    
    print("El área del cuadrado es =", cuadrado.calcular_area())
    print("El perímetro del cuadrado es =", cuadrado.calcular_perimetro())
    print()
    
    print("El área del triángulo es =", triangulo.calcular_area())
    print("El perímetro del triángulo es =", triangulo.calcular_perimetro())
    triangulo.determinar_tipo_triangulo()

if __name__ == "__main__":
    main()
