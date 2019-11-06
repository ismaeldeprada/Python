"""
#P6E9 - AUTOR: ISMAEL DE PRADA

Escribe un programa que te pida nombres de personas
y sus números de teléfono. Para terminar debe pulsar
 “S” cuando te pida el nombre. El programa termina
 escribiendo nombres y números de teléfono. Nota:
  La lista en la que se guardan los nombres y números
   de teléfono tiene esta estructura[[nombre1, telef1],
    [nombre2, telef2], [nom3, telef3], etc], es decir, lista de listas.


"""
listaNombres=list()
nom=(input("Escribe el nombre"))
listaNombres.append(nom)
num = int(input("Escribe el numero de telefono"))
listaNombres.append(num)
while (nom!="s" and nom!="S"):
    nom = (input("Escribe el nombre"))
    listaNombres.append(nom)
    if (nom!="S" and nom!="s"):
        num = int(input("Escribe el numero de telefono"))
        listaNombres.append(num)
listaNombres.remove(-1)
for i in range (len(listaNombres)):
       print (listaNombres[i], end=' ')