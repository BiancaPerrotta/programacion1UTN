import funciones2

#parcial 2 programacion
adn_list=[]  #lista para guardar las secuencias de adn
print("Ingrese las secuencias de ADN por favor:")
for i in range(6): # inicio un bucle for para ingresar en el las 6 cadenas de adn 
    print("Secuencia",(i+1),":")
    adn = input().strip().upper() #se le pide al usuario las cadenas, de ser ingresadas con espacios o en minuscula se modificara con las funciones STRIP y UPPER
    if len(adn) !=6 or any(letter not in "ATCG" for letter in adn):  #si la secuencia ingresada no tiene una long de 6 o si ingresa una letra no correspondida, se sale del programa
        print("Secuencia inválida. Saliendo del programa...")
        exit()
    else:
        adn_list.append(adn)  #si las secuencias son correctas, se guardan en la lista
    
#muestro la matriz creada:
print("----- MATRIZ -----")
for row in adn_list:
    print(" ".join(row))

#invoco a la funcion
result = funciones2.is_mutant(adn_list)
if result == True:
    print("Su individuo es un mutante")
elif result == False:
    print("Su individuo no es un mutante")

