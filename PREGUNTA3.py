#pregunta 3
#Crea una clase llamada Alumno que tenga los atributos nombre y nota
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
alumno1 = Alumno("Juan", 8.5)
alumno2 = Alumno("Maria", 9.2)




#Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
       # print(f"Se ha creado el alumno {self.nombre} con éxito")
alumno1 = Alumno("Juan", 8.5)

#Crear un método llamado calificación que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"Se ha creado el alumno {self.nombre} con éxito")

    def calificacion(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado con una nota de {self.nota}")
        else:
            print(f"El alumno {self.nombre} ha suspendido con una nota de {self.nota}")
alumno1 = Alumno("Juan", 8.5)
alumno1.calificacion()


#crea algunos alumnos
alumno1 = Alumno("Juan", 8.5)
alumno2 = Alumno("Maria", 9.2)
alumno3 = Alumno("Pedro", 4.9)
alumno1.calificacion()
alumno2.calificacion()
alumno3.calificacion()

#Prueba a ejecutar el método calificación de cada objeto que has creado, #hacer los tests



