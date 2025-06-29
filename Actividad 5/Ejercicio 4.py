class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []  # Lista para almacenar programadores

    def esta_lleno(self):
        return len(self.programadores) >= 3  # Máximo 3 programadores

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)

    @staticmethod
    def validar_campo(campo):
        if any(char.isdigit() for char in campo):
            raise Exception("El nombre no puede tener dígitos.")
        if len(campo) >= 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")

    @staticmethod
    def main():
        try:
            nombre_equipo = input("Nombre del equipo: ")
            universidad = input("Universidad: ")
            lenguaje_programacion = input("Lenguaje de programación: ")
            equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje_programacion)

            print("Datos de los integrantes del equipo:")
            for i in range(3):
                nombre_programador = input(f"Nombre del integrante {i + 1}: ")
                EquipoMaratonProgramacion.validar_campo(nombre_programador)

                apellidos_programador = input(f"Apellidos del integrante {i + 1}: ")
                EquipoMaratonProgramacion.validar_campo(apellidos_programador)

                programador = Programador(nombre_programador, apellidos_programador)
                equipo.anadir(programador)

            print("Equipo creado con éxito.")
        except Exception as e:
            print(e)

# Ejecutar el método main
if __name__ == "__main__":
    EquipoMaratonProgramacion.main()
