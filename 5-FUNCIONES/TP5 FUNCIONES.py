from funciones import *

def condition(dni):
    if len(str(dni)) == 7 or len(str(dni)) == 8:
        option = True
        return option
    else:
        option = False
        return option

print("Ejercicio 1:")
dni = int(input("Ingrese su numero de DNI por favor:"))
result = condition(dni)
print("Su numero de DNI es", result)

