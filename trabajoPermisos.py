mensaje = 'Hola, este es el primer ejercicio del modulo 8 del curso de Python basico de OpenBootcamp'

with open('mifichero.txt3', 'w') as f:
    f.write(mensaje)

with open('mifichero.txt3', 'r') as f:
    datos = f.read()
    print(datos)
