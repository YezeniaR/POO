def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            numero_linea = 1  # Contador para el número de línea
            for linea in archivo:
                print(f"Línea {numero_linea}: {linea.strip()}")
                numero_linea += 1
    except IOError:
        print("No se pudo leer el archivo.")

def main():
    nombre_archivo = "C:/prueba.txt"  # Definición del archivo de texto a leer
    leer_archivo(nombre_archivo)

# Ejecutar el método main
if __name__ == "__main__":
    main()
