"""
#P6E3 - AUTOR: ISMAEL DE PRADA
Escribe un programa que pida notas y los guarde en una
lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y
10. El programa termina escribiendo la lista de notas."""
listaNotas =list()
nota = float(input("Escribe una nota  "))
listaNotas.append(nota)
while nota<10 and nota>0:
    nota = float( input("Escribe otra nota  "))
print(listaNotas)