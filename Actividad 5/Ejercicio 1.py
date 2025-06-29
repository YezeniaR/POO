class PruebaExcepciones:
    @staticmethod
    def main():
        # Primer bloque try
        try:
            print("Ingresando al primer try")
            cociente = 10000 / 0  # Se lanza una excepción
            print("Después de la división") 
        except ZeroDivisionError as e:  # Se captura la excepción
            print("División por cero")  
        finally:
            print("Ingresando al primer finally")

        # Segundo bloque try
        try:
            print("Ingresando al segundo try")
            objeto = None
            str(objeto)  # Se lanza una excepción
            print("Imprimiendo objeto")
        except ZeroDivisionError as e:
            print("División por cero")
        except Exception as e:  # Se captura la excepción
            print("Ocurrió una excepción")  # Se imprime en pantalla este mensaje
        finally:
            print("Ingresando al segundo finally")


# Ejecutar el método main
if __name__ == "__main__":
    PruebaExcepciones.main()

