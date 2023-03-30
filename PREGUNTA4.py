class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def calificacion(self):
        if self.nota >= 5:
            return "Aprobado"
        else:
            return "Suspendido"

    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}, Calificación: {self.calificacion()}"

# Creamos algunos objetos de la clase Alumno
alumno1 = Alumno("Juan", 8.5)
alumno2 = Alumno("Maria", 9.2)
alumno3 = Alumno("Pedro", 4.9)

# Imprimimos la información de los objetos utilizando el método print
print(alumno1)
print(alumno2)
print(alumno3)


