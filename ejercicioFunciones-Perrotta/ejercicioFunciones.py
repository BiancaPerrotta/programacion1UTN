from funciones import*  
total_add = 0
while True:
    number = int(input("Ingrese un numero, para terminar ingrese 0: "))
    if number == 0 :
        print("Saliendo...")
        break
    else:
        result = add_digits(number)
        print("La suma de los digitos es",number,"=",result)
        total_add += number
print("La suma de los numeros es de:",total_add)
print("La suma de los digitos es de:", total_add,"=",add_digits(total_add))       


    