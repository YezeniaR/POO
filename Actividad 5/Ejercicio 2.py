class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None  # Inicializamos la edad como None

    def imprimir(self):
        print(f"Nombre del vendedor = {self.nombre}")
        print(f"Apellidos del vendedor = {self.apellidos}")
        print(f"Edad del vendedor = {self.edad}")

    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        self.edad = edad

    @staticmethod
    def main():
        nombre = input("Nombre del vendedor: ")
        apellidos = input("Apellidos del vendedor: ")
        vendedor = Vendedor(nombre, apellidos)
        edad = int(input("Edad del vendedor: "))
        try:
            vendedor.verificar_edad(edad)
            vendedor.imprimir()
        except ValueError as e:
            print(e)

# Ejecutar el método main
if __name__ == "__main__":
    Vendedor.main()
