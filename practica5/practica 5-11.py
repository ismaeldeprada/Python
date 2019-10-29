"""
#P5E11 - AUTOR: ISMAEL DE PRADA
Escribe un programa que pida un número e imprima todos sus divisores.
Dame un número: 200
Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200
"""
num = int(input("Escribe un numerito"))

for i in range(1,num):
    if (num%i==0):
        print (i,"es divisor")


