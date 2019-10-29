"""
#P5E9 - AUTOR: ISMAEL DE PRADA
Escribe un programa que pida la anchura y la altura de un rectángulo y lo dibuje de la siguiente manera:
Anchura del rectángulo: 5
Altura del rectángulo: 4
*****
*   *
*   *
*****
"""

anchura=int(input("Escibe la anchura del rectangulo "))
altura=int(input("Escribe la altura del rectángulo "))

print(anchura * "*")

for i in range(altura-2):
    print("*",(" "*(anchura-4)),"*")
print(anchura * "*")

