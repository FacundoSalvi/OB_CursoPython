class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def resultado(self):
        if self.nota >= 6:
            print("Felicidades", self.nombre, " aprobaste")

        else:
            print(self.nombre, " desaprobaste")

alumno = Alumno("Facundo", 6)
alumno.imprimir()
alumno.resultado()