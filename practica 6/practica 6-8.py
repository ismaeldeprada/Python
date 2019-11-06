"""
#P6E8 - AUTOR: ISMAEL DE PRADA
Escribe un programa que te pida primero un número y
luego te pida números hasta que la suma de los números
introducidos coincida con el número inicial.
 El programa termina escribiendo la lista de números.
"""
numlim = int(input("Escribe el numero limite"))
suma=0
listaNum=list()

while suma!=numlim:
    numsum =int(input("Añada un numero que sumar"))
    if (suma+numsum<=numlim):
        listaNum.append(numsum)
        suma =numsum + suma
    elif (suma+numsum>numlim):
        print("Añada un numero que sumar")
print("El limite a superar es",numlim,)
print("La lista creada es:")
for i in range (len(listaNum)):
       print (listaNum[i], end=' ')







