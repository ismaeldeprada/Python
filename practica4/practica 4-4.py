n1 = int(input("Introduzca un numero"))
n2 = int(input("Introduzca otro  numero"))
n3 = int(input("Introduzca otro  numero"))
n4 = int(input("Introduzca un ultimo numero"))
if (n4%n1==0 and n4%n2==0 and n4%n3==0):
    print("El ultimo numero es divisor de los otros ")
else:
    print("El ultimo numero no es divisor de los otros ")