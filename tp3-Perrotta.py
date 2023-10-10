#1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Ingrese una palabra por favor:")

for i in range(10) :
    print ((i+1),word)



#2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age = int(input("Ingrese su edad:"))

for i in range(age):
    print((i+1),"año/s cumplido")


#3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
num = int(input("Ingrese un numero entero positivo:"))

for i in range(num):
    if i%2 !=0:
        print (i,",", end="")

#4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
num = int(input("Ingrese un numero entero positivo:"))
   
for i in range(num,-1,-1):
    print (i,", ", end="")

#5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
investment=int(input("Ingrese la cantidad de dinero que desea invertir:"))
interest = int(input("Ingrese el interes anual:"))
years = int (input("Ingrese la cantidad de años:"))

interest2 = (interest * investment) /100
capital = investment + interest2
print ("Capital obtenido por año $", capital)
print("Capital obtenido por los",years,"años: $",(capital*years))
    
