def fact(valor):
    f=1
    for i in range (valor):
        f=f*(i+1)
    return f
x=int(input("Ingrese un número: "))
print (fact(x))
