def exponente(valor):
    valor=int(input("Ingrese un número: "))
    if valor==0:
        return 1
    else:
        valor=valor*exponente(valor-1)
        return valor
print(f"El factorial de 4 es {exponente(4)}")
