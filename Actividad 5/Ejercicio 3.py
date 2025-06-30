import math
import tkinter as tk
from tkinter import ttk, messagebox

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ValueError("El valor debe ser un número positivo para calcular el logaritmo")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:  # Nota: 0 es válido para raíz cuadrada
            raise ValueError("El valor debe ser un número positivo para calcular la raíz cuadrada")
        return math.sqrt(valor)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos Numéricos")
        self.root.geometry("400x300")
        
        # Configuración de la interfaz
        self.setup_ui()

    def setup_ui(self):
        # Entrada para el valor numérico
        ttk.Label(self.root, text="Valor numérico:").pack(pady=10)
        self.valor_entry = ttk.Entry(self.root)
        self.valor_entry.pack(pady=5)

        # Botón para calcular
        self.calculate_button = ttk.Button(self.root, text="Calcular", command=self.calcular)
        self.calculate_button.pack(pady=10)

    def calcular(self):
        try:
            valor = float(self.valor_entry.get())
            resultados = []

            # Calcular logaritmo neperiano
            try:
                log_result = CalculosNumericos.calcular_logaritmo_neperiano(valor)
                resultados.append(f"Logaritmo neperiano: {log_result}")
            except ValueError as e:
                resultados.append(str(e))

            # Calcular raíz cuadrada
            try:
                raiz_result = CalculosNumericos.calcular_raiz_cuadrada(valor)
                resultados.append(f"Raíz cuadrada: {raiz_result}")
            except ValueError as e:
                resultados.append(str(e))

            # Mostrar resultados
            messagebox.showinfo("Resultados", "\n".join(resultados))

        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número válido")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

