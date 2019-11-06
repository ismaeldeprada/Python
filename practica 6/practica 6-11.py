"""
#P6E11 - AUTOR: ISMAEL DE PRADA
Escribir un programa para jugar a adivinar un número
(el ordenador "piensa" el número y el usuario lo ha de
adivinar). El programa empieza pidiendo entre qué
números está el número a adivinar, se "inventa" un
número al azar y luego el usuario va probando valores.
El programa va decidiendo si son demasiado grandes o
pequeños. pista:
"""
import random
import time
random.seed (time.time ())

minimo = int(input("Valor minimo  "))
maximo = int (input("Valor maximo "))

secreto = random.randint (minimo, maximo)
numero = int(input("Intenta adivinar el numerito"))
Suma = 1

while (numero!=secreto):
    if numero>secreto:
        numero = int(input("Demasiado grande, Vuelve a probar!"))
    elif (numero<secreto):
        numero = int(input("Demasiado pequeño,Vuelve a probar!  "))
    Suma+=1
print("Correcto!,")
print(Suma,"Intentos")

