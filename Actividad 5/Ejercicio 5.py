import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = ""
            numero_linea = 1  # Contador para el número de línea
            for linea in archivo:
                contenido += f"Línea {numero_linea}: {linea.strip()}\n"
                numero_linea += 1
            return contenido
    except IOError:
        raise Exception("No se pudo leer el archivo.")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lectura de Archivos")
        self.root.geometry("300x300")
        
        # Configuración de la interfaz
        self.setup_ui()

    def setup_ui(self):
        # Entrada para el nombre del archivo
        ttk.Label(self.root, text="Nombre del archivo:").pack(pady=10)
        self.nombre_archivo_entry = ttk.Entry(self.root)
        self.nombre_archivo_entry.pack(pady=5)

        # Botón para leer el archivo
        self.read_button = ttk.Button(self.root, text="Leer Archivo", command=self.leer_archivo)
        self.read_button.pack(pady=10)

        # Cuadro de texto para mostrar el contenido del archivo
        self.result_text = scrolledtext.ScrolledText(self.root, width=50, height=10)
        self.result_text.pack(pady=10)

    def leer_archivo(self):
        nombre_archivo = self.nombre_archivo_entry.get()
        self.result_text.delete(1.0, tk.END)  # Limpiar el cuadro de texto

        try:
            contenido = leer_archivo(nombre_archivo)
            self.result_text.insert(tk.END, contenido)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
