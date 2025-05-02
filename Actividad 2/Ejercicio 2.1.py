class Persona:
    def __init__(self, nombre, apellidos, documento_identidad, año_nacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.documento_identidad = documento_identidad
        self.año_nacimiento = año_nacimiento
    
    def imprimir(self):
        print("Nombre =", self.nombre)
        print("Apellidos =", self.apellidos)
        print("Número de documento de identidad =", self.documento_identidad)
        print("Año de nacimiento =", self.año_nacimiento)
        print()

def main():
    p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
    p2 = Persona("Luis", "León", "1053223344", 2001)
    p1.imprimir()
    p2.imprimir()

if __name__ == "__main__":
    main()
