#P5E8 - AUTOR: ISMAEL DE PRADA
#Escribe un programa que pida la anchura de un triángulo
# y lo dibuje de la siguiente manera:"""

altura = int(input("Escriba la anchura del triangulo"))
suma=0
anchura =altura
for i in range (altura):
    suma=suma+1
    print("*"*suma)
for i in range(altura):
    suma=suma-1
    print("*"*suma)