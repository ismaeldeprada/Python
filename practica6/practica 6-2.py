"""
P6E2 - AUTOR: ISMAEL DE PRADA
Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.
"""

listaNum = list()
num = input("Escribe un numero/escribe salir para terminar")
listaNum.append(num)
while (num!= "salir"):
    num =input("Escribe otro numero/escribe salir para terminar ")
    listaNum.append(num)
listaNum.remove("salir")