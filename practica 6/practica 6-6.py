"""
#P6E6 - AUTOR: ISMAEL DE PRADA
Escribe un programa que pida primero dos números
(máximo y mínimo) y que después te pida números
intermedios. Para terminar de escribir números,
escribe un número que no esté comprendido entre
 los dos valores iniciales.
 El programa termina escribiendo la lista de números.
"""
n1 = int (input("Escribe un numero  "))
n2 = int(input("Escribe un numero mayor al otro numero "))
listaNum=list()
while n1>n2:
   if n1>=n2:
        n2 = int(input("Escribe un numero mayor al otro numero "))
n3 = int(input("Escribe un numero intermedio"))
listaNum.append(n3)
while n3>n1 and n3<n2:
    n3 = int(input("Escribe un numero intermedio"))
    listaNum.append(n3)
listaNum.remove(listaNum[-1])
print("Los numeros intermedios son:")
for i in range (len(listaNum)):
       print (listaNum[i], end=' ')



