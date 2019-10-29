d = int(input("Introduzca la cantidad "))
if d%500==0 and d>0:
    x=d/500
    print ("el cajero le devuelve",x ,"billetes de 500 euros")
elif d%200==0 and d>0:
    x=d/200
    print  ("el cajero le devuelve", x, "billetes de 200 euros")
elif d%100==0 and d>0:
    x=d/100
    print  ("el cajero le devuelve", x,"billetes de 100 euros")
elif d%50==0 and d>0:
    x=d/50
    print  ("el cajero le devuelve", x,"billetes de 50 euros")
elif d%5==0 and d>0:
    x=d/5
    print  ("el cajero le devuelve", x,"billetes de 5 euros")
