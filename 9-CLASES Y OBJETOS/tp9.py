print("Ejercicio 1:")
class Person:
    def __init__(self,name=None,age=None,dni=None):
        self.name = name
        self.age = age
        self.dni = dni

    #setters
    def set_name(self,name):
        self.__name = name.capitalize()

    def set_age(self,age):
        if age < 0:
            print("ERROR. La edad no puede ser negativa\n Saliendo del programa...")
        else:
            self.__age = age


    def set_dni(self,dni):
        if len(str(dni)) < 7 or len(str(dni)) > 8:
            print("ERROR. El dni ingresado es invalido\n Saliendo del programa...")
        else:
            self.__dni = dni

    #getters
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_dni(self):
        return self.__dni
    
    #muestro los datos de la persona
    def show_person(self):
        print("NOMBRE:",self.__name)
        print("EDAD:",self.__age)
        print("DNI:",self.__dni)

    #funcion para saber si el usuario es mayor o menor de edad
    def is_grater(self):
        if self.__age > 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

#PROGRAMA PRINCIPAL:
person = Person()
person.set_name(input("Ingrese su nombre:"))
person.set_age(int(input("Ingrese su edad:")))
person.set_dni(int(input("Ingrese su DNI:")))
person.is_grater()

print("Ejercicio 2:")
class Account:
    def __init__(self,headline=None,quantity=0.0):
        self.headline = headline
        self.quantity = quantity

    #setters
    def set_headline(self,headline):
        self.__headline = headline.capitalize()    

    def set_quantity(self,quantity):
        self.__quantity = quantity

    #getters
    def get_headline(self):
        return self.headline
    
    def get_quantity(self):
        return self.quantity
    
    #mostrar datos:
    def show_account(self):
        print("NOMBRE:",self.headline)
        print("CANTIDAD: $",self.quantity)

    #ingreso de dinero
    def income (self,quantity):
        if quantity > 0:
            self.quantity += quantity

    #retiro de dinero
    def retreat (self,quantity):
        if quantity > 0:
            self.quantity -= quantity

#PROGRAMA PRINCIPAL:
account = Account("Bianca Perrotta",250.000)
account.show_account()
account.income(10.000)
account.retreat(50.000)
account.show_account()

print("Ejercicio 3:")
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def print_largest_side(self):
        print("El lado mayor es el de", max(self.side1, self.side2, self.side3), "cm") 
    
    def triangle_type(self):
        if self.side1 == self.side2 and self.side2 == self.side3:
            print("TRIÁNGULO EQUILÁTERO")
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            print("TRIÁNGULO ISÓCELES")
        else:
            print("TRIÁNGULO ESCALENO")

    #setters
    def set_side1(self, side1):
        if side1 > 0:
            self.__side1 = side1
    
    def set_side2(self, side2):
        if side2 > 0:
            self.__side2 = side2
    
    def set_side3(self, side3):
        if side3 > 0:
            self.__side3 = side3
    
    #getters
    def get_side1(self):
        return self.__side1
    
    def get_side2(self):
        return self.__side2
    
    def get_side3(self):
        return self.__side3

#PROGRAMA PRINCIPAL:
triangle = Triangle(7,9,9)
triangle1 = Triangle(15,10,5)
triangle2 = Triangle(3,3,3)
triangle.triangle_type()
triangle.print_largest_side()
triangle1.triangle_type()
triangle2.triangle_type()

        
