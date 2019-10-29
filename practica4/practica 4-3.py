
i = input("pulse T para calcular el area de un triangulo o C para calcular el area de un cuadrado ")
if i==("t"):
    b = int(input("escribe base del triangulo "))
    h = int(input("escribe la altura del triangulo"))
    rt = (b*h/2)
    print("el area del triangulo es",rt)
elif i==("c"):
    l = float (input("introduce la medida de los costados"))
    rc = (l*l)
    print ("el area del cuadrado es",rc)

