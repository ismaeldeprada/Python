"""
#P6E7 - AUTOR: ISMAEL DE PRADA
Escribe un programa que pida un número (límite) y
luego te pida números hasta que la suma de los números introducidos
 supere el límite inicial.
El programa termina escribiendo la lista de números.
"""
numlim = int(input("Escribe el numero limite"))
suma=0
listaNum=list()
while suma<numlim:
    numsum =int(input("Añada un numero que sumar"))
    listaNum.append(numsum)
    suma=suma+numsum
print("El limite a superar es",numlim,)
print("Los numeros intermedios son:")
for i in range(len(listaNum)):
       print(listaNum[i], end=' ')
       
