"""
#P6E5 - AUTOR: ISMAEL DE PRADA
Escribe un programa que te pida números cada vez más
 grandes y que se guarden en una lista.
  Para acabar de escribir los números,
  escribe un número que no sea mayor que el anterior.
  El programa termina escribiendo la lista de números:
"""
n1 = int(input("Escribe un numero"))
listaPalabras = list()
listaPalabras.append(n1)
n2 = int(input("Escribe un numero mayor"))
contador = 0
if n2>n1:
    while (n2>listaPalabras[contador]):
        contador+=1
        listaPalabras.append(n2)
        n2 = int(input("Escribe un numero mayor"))
print ("Los números que has escrito son:")
for i in range (len(listaPalabras)):
    print(listaPalabras[i], end=' ')