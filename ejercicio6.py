class Vehiculo:
    color = None
    ruedas = 0
    puertas = 0
    def __init__(self):
        self.color = "Rojo"
        self.ruedas = 8
        self.puertas = 2


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0
    def __init__(self):
        self.color = "Verde"
        self.ruedas = 4
        self.puertas = 4
        self.velocidad = 220
        self.cilindrada = 2.0

miObjeto = Coche()

print ("el color del coche es ", miObjeto.color)
print("El coche tiene ", miObjeto.ruedas, " ruedas")
print("El numero de puertas del coche es de: ", miObjeto.puertas)
print("La velocidad maxima del coche es de: ", miObjeto.velocidad)
print("La cilindrada del motor del coche es de", miObjeto.cilindrada)