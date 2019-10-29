"""
#P5E10 - AUTOR: ISMAEL DE PRADA
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura de un triángulo: 5
    *
   ***
  *****
 *******
*********
"""
filas = int(input("Introduzca la altura del triangulo"))
#(' '*(filas-i-1) hace espacios
#'*'*(2*i+1)) hace los arteriscos
for i in range(filas):
    print(' '*(filas-i-1)+'*'*(2*i+1))
