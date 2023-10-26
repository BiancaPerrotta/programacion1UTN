
def condition(dni):  #funcion condition para validar si el DNI es valido(true) o invalido(false)
    if len(str(dni)) == 7 or len(str(dni)) == 8:  #con la funcion len corroboro el largo de la cadena(debe ser =7 o =8)
        option = True
        return option
    else:
        option = False
        return option

print("Ejercicio 1:")
dni = int(input("Ingrese su numero de DNI por favor:"))
result = condition(dni) #invoco la funcion de condition
print("Su numero de DNI es", result)





def long (oration):
    oration = oration.strip() #la funcion strip elimina los espacios
    word = oration.split() #la funcion split divide la oracion en palabras
    if word:
        return len(word[-1]) #retornamos la long de la ultima palabra
    else:
        return 0

print("Ejercicio 2:")
oration = "Hola soy Bianca"
longer = long(oration)
print("La longitud de la ultima palabra es de:",longer)

def identifier(name,last_name,dni):
    digits = dni[:3] #saco los 3 primeros digitos de dni
    print(name, len(last_name), digits, sep="") #imprimo los datos del identificador y con la funcion sep saco el espacio entre ellas
    return



print("Ejercicio 3")
print("Bienvenid@ al club UTN, ingrese los datos solicitados para obtener su identificador, si desea terminar ejecute un espacio vacio. GRACIAS!!! ")

while True:  #inicio un bucle while para repetir el proceso con cuantos socios se desee
    name = input("Ingrese su nombre:")
    if name == " ": #si se ingresa un espacio vacio como nombre, se sale del bucle
        print("SALIENDO...")
        break
    last_name = input("Ingrese su apellido por favor:")
    while True:  #inicio otro bucle while para corroborar que el dni sea valido
        dni = input("Por ultimo, ingrese su DNI:")
        if len(str(dni)) == 7 or len(str(dni)) == 8:  
            print("DNI correcto")
            break
        else: #de no serlo, se lo solicitara las veces necesarias para continuar
            print("DNI invalido, ingrese nuevamente:")
    result = identifier(name,last_name,dni) #llamo a la funcion identifier


def multiplo(number1,number2):
    if number1 % number2 == 0: #verifico si el num1 es multiplo del num2
        print("El numero 1 es multiplo del numero 2")
    else:
        print("El numero 1 NO es multiplo del numero 2")
    return



print("Ejercicio 4")   
number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero para corroborar si es multiplo del primero: "))
multiplo(number1,number2)


def medium_temperature(max_temperature,min_temperature):
    medium = (max_temperature + min_temperature) / 2  #calculo la temperatura media 
    return medium

print("Ejercicio 5")
days = int(input("Ingrese la cantidad de dias a calcular:"))

for i in range(days):  #con el bucle for voy pidiendo las temperaturas por los dias solicitados por el usuario
    max_temperature = int(input("Ingrese la temperatura maxima: "))
    min_temperature = int(input("Ingrese la temperatura minima: "))
    print("La temperatura media es:",medium_temperature(max_temperature,min_temperature))


def function_space(oration):
    letters = " ".join(oration) # uso la funcion join para separar las letras con un espacio extra
    return letters


print("Ejercicio 6")
oration = "Hola como estas"
print(function_space(oration))