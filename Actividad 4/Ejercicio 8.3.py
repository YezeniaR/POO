import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def calcular_volumen(self):
        pass

    def calcular_superficie(self):
        pass

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio ** 2)

    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_base = 2 * math.pi * (self.radio ** 2)
        return area_lateral + area_base

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4/3) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        return 4 * math.pi * (self.radio ** 2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("350x160")
        self.crear_componentes()

    def crear_componentes(self):
        tk.Button(self, text="Cilindro", command=self.ventana_cilindro).pack(pady=10)
        tk.Button(self, text="Esfera", command=self.ventana_esfera).pack(pady=10)
        tk.Button(self, text="Pirámide", command=self.ventana_piramide).pack(pady=10)

    def ventana_cilindro(self):
        VentanaCilindro()

    def ventana_esfera(self):
        VentanaEsfera()

    def ventana_piramide(self):
        VentanaPiramide()

class VentanaCilindro(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Cilindro")
        self.geometry("280x210")
        self.crear_componentes()

    def crear_componentes(self):
        tk.Label(self, text="Radio (cms):").grid(row=0, column=0)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.grid(row=0, column=1)

        tk.Label(self, text="Altura (cms):").grid(row=1, column=0)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.grid(row=1, column=1)

        tk.Button(self, text="Calcular", command=self.calcular).grid(row=2, columnspan=2)

        self.label_volumen = tk.Label(self, text="Volumen (cm³):")
        self.label_volumen.grid(row=3, columnspan=2)

        self.label_superficie = tk.Label(self, text="Superficie (cm²):")
        self.label_superficie.grid(row=4, columnspan=2)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            altura = float(self.campo_altura.get())
            cilindro = Cilindro(radio, altura)
            self.label_volumen.config(text=f"Volumen (cm³): {cilindro.volumen:.2f}")
            self.label_superficie.config(text=f"Superficie (cm²): {cilindro.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaEsfera(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("280x200")
        self.crear_componentes()

    def crear_componentes(self):
        tk.Label(self, text="Radio (cms):").grid(row=0, column=0)
        self.campo_radio = tk.Entry(self)
        self.campo_radio.grid(row=0, column=1)

        tk.Button(self, text="Calcular", command=self.calcular).grid(row=1, columnspan=2)

        self.label_volumen = tk.Label(self, text="Volumen (cm³):")
        self.label_volumen.grid(row=2, columnspan=2)

        self.label_superficie = tk.Label(self, text="Superficie (cm²):")
        self.label_superficie.grid(row=3, columnspan=2)

    def calcular(self):
        try:
            radio = float(self.campo_radio.get())
            esfera = Esfera(radio)
            self.label_volumen.config(text=f"Volumen (cm³): {esfera.volumen:.2f}")
            self.label_superficie.config(text=f"Superficie (cm²): {esfera.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaPiramide(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Pirámide")
        self.geometry("280x240")
        self.crear_componentes()

    def crear_componentes(self):
        tk.Label(self, text="Base (cms):").grid(row=0, column=0)
        self.campo_base = tk.Entry(self)
        self.campo_base.grid(row=0, column=1)

        tk.Label(self, text="Altura (cms):").grid(row=1, column=0)
        self.campo_altura = tk.Entry(self)
        self.campo_altura.grid(row=1, column=1)

        tk.Label(self, text="Apotema (cms):").grid(row=2, column=0)
        self.campo_apotema = tk.Entry(self)
        self.campo_apotema.grid(row=2, column=1)

        tk.Button(self, text="Calcular", command=self.calcular).grid(row=3, columnspan=2)

        self.label_volumen = tk.Label(self, text="Volumen (cm³):")
        self.label_volumen.grid(row=4, columnspan=2)

        self.label_superficie = tk.Label(self, text="Superficie (cm²):")
        self.label_superficie.grid(row=5, columnspan=2)

    def calcular(self):
        try:
            base = float(self.campo_base.get())
            altura = float(self.campo_altura.get())
            apotema = float(self.campo_apotema.get())
            piramide = Piramide(base, altura, apotema)
            self.label_volumen.config(text=f"Volumen (cm³): {piramide.volumen:.2f}")
            self.label_superficie.config(text=f"Superficie (cm²): {piramide.superficie:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()

