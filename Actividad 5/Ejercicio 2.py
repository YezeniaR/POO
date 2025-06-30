import tkinter as tk
from tkinter import ttk, messagebox

class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = None  # Inicializamos la edad como None

    def imprimir(self):
        return (f"Nombre del vendedor = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor = {self.edad}")

    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        self.edad = edad

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vendedor")
        self.root.geometry("300x300")
        
        # Configuración de la interfaz
        self.setup_ui()

    def setup_ui(self):
        # Entradas para nombre y apellidos
        ttk.Label(self.root, text="Nombre del vendedor:").pack(pady=5)
        self.nombre_entry = ttk.Entry(self.root)
        self.nombre_entry.pack(pady=5)

        ttk.Label(self.root, text="Apellidos del vendedor:").pack(pady=5)
        self.apellidos_entry = ttk.Entry(self.root)
        self.apellidos_entry.pack(pady=5)

        ttk.Label(self.root, text="Edad del vendedor:").pack(pady=5)
        self.edad_entry = ttk.Entry(self.root)
        self.edad_entry.pack(pady=5)

        # Botón para registrar vendedor
        self.register_button = ttk.Button(self.root, text="Registrar Vendedor", command=self.registrar_vendedor)
        self.register_button.pack(pady=10)

    def registrar_vendedor(self):
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        edad_str = self.edad_entry.get()

        try:
            edad = int(edad_str)
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)
            messagebox.showinfo("Éxito", vendedor.imprimir())
        except ValueError as e:
            messagebox.showerror("Error", str(e))

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
