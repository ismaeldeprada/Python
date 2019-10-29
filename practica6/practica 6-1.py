"""
P6E1 - AUTOR: ISMAEL DE PRADA
Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras."""

listaPalabras = list()
palabra = input("Escribe una palabra/pulsa enter para terminar")
listaPalabras.append(palabra)
while (palabra!= ""):
    palabra =input("Escribe otra palabra/pulsa enter para terminar ")
    listaPalabras.append(palabra)
listaPalabras.remove("")
