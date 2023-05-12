import math
import random
#from random import*



v=[None]*10
print (v)


v[3]=56
print (v)

v.pop()
print (v)

v[3]='Hola'
print(v)
v[2]=100

v.append(90)
print (v)



#dim=int(input("Digite la dimensión del vector: "))

#v2=[0]*dim

#print(v2)

#for i in range (0,dim):
   # valor=int(input("Digite un número: "))
   # v2[i]=valor
#print (v2)

#v2.sort()
#print (v2)



dim=int(input("Digite la dimensión del vector: "))


v2=[0]*dim
mayor=-math.inf
menor=math.inf
suma=0

for i in range (0,dim):
    valorRand=random.randint(1,1000)
    v2[i]=valorRand
    if (v2[i]>mayor):
        mayor=v2[i]
    if (v2[i]<menor):
        menor=v2[i]
    suma=v2[i]+suma
print (v2)
promedio=suma/dim
print ("El mayor es: ",mayor)
print ("El menor es: ",menor)
print("El promedio es: ", promedio)







