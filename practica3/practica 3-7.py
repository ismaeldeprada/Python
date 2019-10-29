d = int (input ("Introduce un dia"))
m = int (input("introduce mes"))
a = int (input("introduce el año"))
if (m>12 or m<1 or d>31 or d<1 or a<=0):
    print ("Fecha incorrecta")

elif (m==2 and d>28  ):
    print ("Fecha incorrecta ")
elif (d>31):
    print ("Fecha incorrecta")
elif (m==4 and d>30):
    print ("Fecha incorrecta")
elif (m==6 and d>30):
    print("Fecha incorrecta")
elif (m==9 and d>30):
    print ("Fecha incorrecta")
elif (m==9 and d>30):
    print("Fecha incorrecta")
else:
    print ("Fecha correcta")






