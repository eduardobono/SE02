'''
###########################
### Autor: Eduardo Bono ###
###  Fecha: 02/03/2022  ###
###     Ejercicio 15    ###
###########################
'''


# ANOTACIONES


# VARIABLES


# FUNCIONES


ventas = input("¿Cuantas ventas has hecho? ")
total = int(input("Introduce el valor de la primera venta: "))
for i in range(2, int(ventas) + 1):
    temporal = int(input("Introduce el valor de la siguiente venta: "))
    total = total + temporal

print("El valor total de las ventas es: ", total)