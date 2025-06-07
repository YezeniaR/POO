import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5  # Crea un array de 5 notas

    def calcular_promedio(self):
        suma = sum(self.lista_notas)
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = sum((nota - prom) ** 2 for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("280x380")
        self.resizable(False, False)

        self.lista_notas = [tk.StringVar() for _ in range(5)]
        self.crear_componentes()

    def crear_componentes(self):
        for i in range(5):
            tk.Label(self, text=f"Nota {i + 1}:").place(x=20, y=20 + i * 30)
            tk.Entry(self, textvariable=self.lista_notas[i]).place(x=105, y=20 + i * 30)

        tk.Button(self, text="Calcular", command=self.calcular).place(x=20, y=170)
        tk.Button(self, text="Limpiar", command=self.limpiar).place(x=125, y=170)

        self.resultados = {
            "promedio": tk.Label(self, text="Promedio = ")
        }
        self.resultados["promedio"].place(x=20, y=210)

        self.resultados["desviacion"] = tk.Label(self, text="Desviación = ")
        self.resultados["desviacion"].place(x=20, y=240)

        self.resultados["mayor"] = tk.Label(self, text="Nota mayor = ")
        self.resultados["mayor"].place(x=20, y=270)

        self.resultados["menor"] = tk.Label(self, text="Nota menor = ")
        self.resultados["menor"].place(x=20, y=300)

    def calcular(self):
        notas = Notas()
        for i in range(5):
            try:
                notas.lista_notas[i] = float(self.lista_notas[i].get())
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
                return

        promedio = notas.calcular_promedio()
        desviacion = notas.calcular_desviacion()
        mayor = notas.calcular_mayor()
        menor = notas.calcular_menor()

        self.resultados["promedio"].config(text=f"Promedio = {promedio:.2f}")
        self.resultados["desviacion"].config(text=f"Desviación = {desviacion:.2f}")
        self.resultados["mayor"].config(text=f"Nota mayor = {mayor:.2f}")
        self.resultados["menor"].config(text=f"Nota menor = {menor:.2f}")

    def limpiar(self):
        for var in self.lista_notas:
            var.set("")
        for label in self.resultados.values():
            label.config(text="")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
