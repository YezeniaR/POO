import tkinter as tk
from tkinter import ttk, messagebox

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

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Equipo de Programación")
        self.root.geometry("400x600")
        
        # Configuración de la interfaz
        self.setup_ui()

    def setup_ui(self):
        # Entradas para el equipo
        ttk.Label(self.root, text="Nombre del equipo:").pack(pady=5)
        self.nombre_equipo_entry = ttk.Entry(self.root)
        self.nombre_equipo_entry.pack(pady=5)

        ttk.Label(self.root, text="Universidad:").pack(pady=5)
        self.universidad_entry = ttk.Entry(self.root)
        self.universidad_entry.pack(pady=5)

        ttk.Label(self.root, text="Lenguaje de programación:").pack(pady=5)
        self.lenguaje_entry = ttk.Entry(self.root)
        self.lenguaje_entry.pack(pady=5)

        # Entradas para los programadores
        self.programador_entries = []
        for i in range(3):
            ttk.Label(self.root, text=f"Nombre del integrante {i + 1}:").pack(pady=5)
            nombre_entry = ttk.Entry(self.root)
            nombre_entry.pack(pady=5)
            self.programador_entries.append((nombre_entry, None))  # Guardar solo el nombre por ahora

            ttk.Label(self.root, text=f"Apellidos del integrante {i + 1}:").pack(pady=5)
            apellidos_entry = ttk.Entry(self.root)
            apellidos_entry.pack(pady=5)
            self.programador_entries[i] = (nombre_entry, apellidos_entry)  # Guardar nombre y apellidos

        # Botón para crear el equipo
        self.create_button = ttk.Button(self.root, text="Crear Equipo", command=self.crear_equipo)
        self.create_button.pack(pady=10)

    def crear_equipo(self):
        try:
            nombre_equipo = self.nombre_equipo_entry.get()
            universidad = self.universidad_entry.get()
            lenguaje_programacion = self.lenguaje_entry.get()
            equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje_programacion)

            for i in range(3):
                nombre_programador = self.programador_entries[i][0].get()
                apellidos_programador = self.programador_entries[i][1].get()

                EquipoMaratonProgramacion.validar_campo(nombre_programador)
                EquipoMaratonProgramacion.validar_campo(apellidos_programador)

                programador = Programador(nombre_programador, apellidos_programador)
                equipo.anadir(programador)

            messagebox.showinfo("Éxito", "Equipo creado con éxito.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
