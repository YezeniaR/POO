class Persona:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}"
    
    def seleccionar_nombre(self, nombre: str):
        self.nombre = nombre
    
    def seleccionar_direccion(self, direccion: str):
        self.direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre
    
    def __str__(self) -> str:
        return f"{super().__str__()}, Carrera: {self.carrera}, Semestre: {self.semestre}"
    
    def seleccionar_carrera(self, carrera: str):
        self.carrera = carrera
    
    def seleccionar_semestre(self, semestre: int):
        self.semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria
    
    def __str__(self) -> str:
        return f"{super().__str__()}, Departamento: {self.departamento}, Categoría: {self.categoria}"
    
    def seleccionar_departamento(self, departamento: str):
        self.departamento = departamento
    
    def seleccionar_categoria(self, categoria: str):
        self.categoria = categoria


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias
    persona1 = Persona("Juan Pérez", "Calle 123")
    estudiante1 = Estudiante("María Gómez", "Avenida 456", "Ingeniería", 5)
    profesor1 = Profesor("Dr. Rodríguez", "Carrera 789", "Matemáticas", "Titular")
    
    # Mostrar información
    print("Información")
    print(persona1)
    print(estudiante1)
    print(profesor1)
    
    # Modificar atributos
    estudiante1.seleccionar_semestre(6)
    profesor1.seleccionar_departamento("Ciencias")
    
    print("\nDespués de modificaciones ")
    print(estudiante1)
    print(profesor1)
