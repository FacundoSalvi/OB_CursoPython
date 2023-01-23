#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
numero = range(1,101)

listaOrdenada = sorted(numero, reverse=True)
print(listaOrdenada)