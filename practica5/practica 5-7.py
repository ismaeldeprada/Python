#P5E7 - AUTOR: ISMAEL DE PRADA
#Escribe un programa que pida la altura de un triángulo y
# lo dibuje de la siguiente manera:"""

altura = int(input("Escribe una altura  "))
suma=altura
for i in range (altura):
    suma=suma-1
    print("*"*suma)
