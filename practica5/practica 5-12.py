"""P5E12 - AUTOR: ISMAEL DE PRADA
#Escribe un programa que pida un número y escriba si primo o no"""
contador = 2
num=int(input("Escribe un numero"))
for i in range (1,num):
    if (num%i)!=0 :
       contador+=1
if (contador == num):
    print("ES PRIMO")
else:
    print ("NO ES PRIMO")


