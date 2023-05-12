from random import *

tamaño=int(input("Ingrese tamaño de la lista: "))
lista1=[]

lista2=[]
ordenado1=[]
ordenado2=[]
mayor1=0
mayor2=0
while tamaño>0:
    for i in range(tamaño):
        lista1.append(randint(1,10))
        for j in range(lista1):
            if lista1[j]>mayor1:
                mayor1=lista1
                
        lista2.append(randint(1,10))
    tamaño=0
print(lista2)
print(lista1)