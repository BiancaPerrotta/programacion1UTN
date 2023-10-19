
name = input("Hola! Ingrese su nombre: ")
print("¡Bienvenido/a,", name, "!")

option = 0
while option != 3:                       # mediante un while pongo como condicion de salida el numero(opcion) 3
    print("\nMenú de opciones:")
    print("1. Juego de números")
    print("2. Juego de palabras")
    print("3. Salir")

    option = int(input("Seleccione una opción: "))        # ingreso la opcion en el menu 

    if option == 1:   # si la opcion es 1, realiza el juego de numeros
        numbers = []  # creo una lista llamada numbers donde van a ser guardados los numeros (number) ingresados
        number = int(input("Ingrese un número entero (0 para salir): "))

        while number != 0: # se ejecuta mientras el numero sea distinto de 0
            numbers.append(number)   # se guarda el numero ingresado en la lista
            number = int(input("Ingrese otro número entero (0 para salir): "))

        number_odd = [num for num in numbers if num % 2 == 0]  #creo una lista de numeros pares utilizando un metodo for para filtrar los pares
        number_even = [num for num in numbers if num % 2 != 0]  # realizo lo mismo pero con los numeros impares

        if len(number_odd) > 0:
            highest_even = max(number_odd)   # encuentro el numero par mayor
            print("El mayor número par es:", highest_even)
        else:
            print("No se ingresaron números pares.")

        if len(number_even) > 0:
            average_even = sum(number_even) / len(number_even)  # saco el promedio de los numeros impares
            print("El promedio de los números impares es:", average_even)
        else:
            print("No se ingresaron números impares.")

    elif option == 2:  # si la opcion es 2, hago el juego de palabras
        sentence = input("Ingrese una frase: ")
        vowels= {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}  # creo un diccionario con las vocales 

        for letter in sentence.lower():  #se inicia un bucle for que recorre cada letra en la cadena de texto convertida a minúsculas mediante el método lower().
            if letter in vowels:      #verificamos si la letra se encuentra en el diccionario
                vowels[letter] += 1   # si es asi, incrementamos el contador de X vocal

        for vowel, quantity in vowels.items():
            print("La cantidad de", vowel, "es:", quantity)  # mostramos los contadores

print("¡Hasta luego, ", name, "!")
    
