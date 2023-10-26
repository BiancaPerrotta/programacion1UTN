#ejercicio 1 INGLES 
print("Ejercicio 1")
x=0

while x<= 30:
    x+=1
   
    if x==4 or x==6 or x==10:
        print("Se ha saltado el valor",x, "de x")
        continue
    elif x == 15:
        print("Se rompio la ejecucion del bucle cuando el valor de x era:",x)
        break
    else:
        print(x)


#ejercicio 2
print("Ejercicio 2")
money = 0
print("Deposito : D + monto a depositar // Retiro: R + monto a retirar // Para salir presione enter")

while True:
    movements = input().upper()
    option = movements[0:1]

    if option == "D":
        money += int(movements[1::])

    elif option == "R":
        money -= int(movements[1::])

    elif option == "":
        print("$",money)
        break
    else:
        print("ERROR")

#ejercicio 3
print("Ejercicio 3")
print("Por favor ingrese numeros mayores a 1, para finalizar ingrese 0 :")
counter = 0

while True:
    counter2 = 0
    num = int(input())
    if num > 1:
        for i in range(1,num+1):   
            if num % i == 0:         
                counter2 += 1
        
        if counter2 == 2:         
            counter += 1
    elif num == 0:
        break
    elif num < 1:
        print ("Numero incorrecto, intentelo de nuevo")
        continue

print ("Cantidad de numeros primos ingresados:", counter)


#ejercicio 4 
print("Ejercicio 4")
print ("Ingrese dos años por favor:")
year = int(input())
year2 = int(input())

for i in range(year,year2+1):
    if (i % 4 == 0) and (i % 100 != 0 or i % 400 == 0) and (i% 10 == 0):
        print("Es un año biciesto:",i)

#ejercicio 5
print("Ejercicio 5")
for i in range(1,20):
    if i % 2 == 0 :
        print (i)
    else:
        continue


#ejercicio 6    
print("Ejercicio 6")
list = [1,2,5,8,0,6]
num = int(input("Ingrese el numero a buscar:"))
found = True

for i in list:
    if num == i:
        print("Numero encontrado")
        found = True
        break
    else:
        found = False

if found == False:
    print("Numero NO encontrado")

#ejercicio 7 
print ("Ejercicio 7")
print("MENU PRINCIPAL")
print("1)Ingresar nombre y apellido\n 2)Ingresar DNI\n 3)Ingresar domicilio\n 0)Salir")

while True:
    option = int (input())
    if option == 1:
        print ("Ingrese su nombre y apellido por favor:")
        name = input()
    elif option == 2:
        print("Ingrese su DNI por favor:")
        DNI = int(input())
    elif option == 3:
        print ("Ingrese su direccion por favor:")
        address = input()
    elif option == 0:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion inválida")
    

