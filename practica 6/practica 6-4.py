"""
#P6E4 - AUTOR: ISMAEL DE PRADA
Escribe un programa que te pida dos números, de manera
que el segundo sea mayor que el primero.
El programa termina escribiendo los dos números tal
y como se pide:
"""
n1 = int(input("Escribe un numero"))
n2 = int(input("Escribe un numero mayor que el primer numero"))
while (n1>n2):
    n2 = int(input("Escribe un numero mayor que el primer numero"))
print("Los numeros que has escrito son ",n1,n2)

