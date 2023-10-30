print("Ejercicio 1")
numbers = []
while True:
    number = int(input("Ingrese numeros enteros por favor, para finalizar ingrese 0: "))
    if number == 0:
        break
    else:
        numbers.append(number)


print("Ejercicio 2:")
num = int(input("Ingrese un numero para ver si esta en la lista: "))
if num in numbers:
    numbers.remove(num)
    print(numbers)
else:
    print("Elemento no encontrado", numbers)


print("Ejercicio 3:")
add = 0
for number in numbers:
    add+=number
print("La suma de los elementos de la lista es = ", add)


print("Ejercicio 4:")
numbers2 = []
num2 = int(input("Ingrese otro numero: "))
for number in numbers:
    if number < num2:
        numbers2.append(number)
print("Nueva lista:",numbers2)



