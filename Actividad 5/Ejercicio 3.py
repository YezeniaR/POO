import math

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        try:
            if valor <= 0:
                raise ValueError("El valor debe ser un número positivo para calcular el logaritmo")
            resultado = math.log(valor)
            print(f"Resultado del logaritmo neperiano = {resultado}")
        except ValueError as e:
            print(e)
            raise  # Re-lanzamos la excepción para que el main pueda detectarla

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        try:
            if valor < 0:  # Nota: 0 es válido para raíz cuadrada
                raise ValueError("El valor debe ser un número positivo para calcular la raíz cuadrada")
            resultado = math.sqrt(valor)
            print(f"Resultado de la raíz cuadrada = {resultado}")
        except ValueError as e:
            print(e)
            raise  # Re-lanzamos la excepción para que el main pueda detectarla

    @staticmethod
    def main():
        try:
            valor = float(input("Valor numérico: "))
            
            try:
                CalculosNumericos.calcular_logaritmo_neperiano(valor)
            except ValueError:
                pass  # Ya se mostró el mensaje
            
            # Luego intentamos la raíz cuadrada
            try:
                CalculosNumericos.calcular_raiz_cuadrada(valor)
            except ValueError:
                pass  # Ya se mostró el mensaje
                
        except ValueError as e:
            print("Error: Debe ingresar un número válido")

if __name__ == "__main__":
    CalculosNumericos.main()
