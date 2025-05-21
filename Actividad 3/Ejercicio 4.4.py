class Profesor:
    def imprimir(self):
        print("Es un profesor.")

class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular.")

# Uso polimórfico
profesor1 = ProfesorTitular()
profesor1.imprimir()  # Salida: "Es un profesor titular."
