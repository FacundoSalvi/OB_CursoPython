##Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

numDia = input("cuantos dias tiene el año en cuestion?")

numDia = int(numDia)
def year(bis = 366, nobis = 365):
    if numDia == bis:
        print ("el año es bisiesto")

    else:
        if numDia == nobis:
            print ("el año no es bisiesto")

        else:
            print("intoduce un numero de días correcto")

year()
