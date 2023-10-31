def digits(number):
    count = 0 #inicializo el contador para ir contando los digitos del numero ingresado
    while number > 0:  
        number = number // 10 #divido el numero entre 10 y me quedo con el resto, que seria el numero anterior, y continuo hasta quedarme sin numeros
        count +=1   #voy contando los digitos con el contador previamente inicializado
    return count


print("Ejercicio 1:")
number = int(input("Ingrese un numero entero positivo:"))
print("El numero tiene",digits(number), "digitos")  #invoco a la recursion


def power(n, b):
    if n == 1: #si n es igual a 1, cualquier numero elevado a cualquier potencia sera 1
        return True  #por eso es verdadero y retornamos TRUE
    if b == 1:   # si b es igual a 1, retornamos a la condicion anterior ya que cualquier número elevado a la potencia 1 es simplemente el número en sí mismo
        return n == 1
    if n < b:  #si n es menor que b es imposible que sea potencia, por lo que retornamos FALSE
            return False
    return power(n / b, b)  #si ninguno de los casos base se cumple, la funcion se llama a si misma 

print("Ejercicio 2:")
n = int(input("Ingrese el primer numero entero: "))
b = int(input("Ingrese el segundo numero entero: "))
print(n,"es potencia de",b,"?:",power(n,b))   #invoco a la recursion

def larger_number(numbers):
    if len(numbers) == 0: #utilizo la funcion len para corroborar si es o no una lista vacia
        return None   #en el caso de serlo, retornamos None ya que no hay valores a evaluar
    elif len(numbers) == 1:  #utilizo nuevamente len para corroborar si la lista tiene o no UN solo elemento
        return numbers[0]  #de ser asi, devolvemos ese unico elemento
    else:   #si la lista tiene mas de un elemento...
        first_element = numbers[0]   #asignamos la variable al primer valor de la lista (89)
        rest_numbers = numbers[1:]   #asignamos la variable al RESTO de la lista 
        first_rest = larger_number(rest_numbers)  #invocamos a la recursividad para evaluar todos los elementos de la lista restantes
        
        if first_element > first_rest: #Si el primer elemento es mayor que el resultado de la llamada recursiva, devuelve el primer elemento como el mayor elemento
            return first_element
        else: #Si el resultado de la llamada recursiva es mayor que el primer elemento, devuelve el resultado de la llamada recursiva como el mayor elemento.
            return first_rest


print("Ejercicio 5:")
numbers = [89,45,2,36,102,65]
result = larger_number(numbers) #invoco la recursion
print("El mayor elemento de la lista es:",result)