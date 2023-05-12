import random as rn

class pila():
    def __init__(self):
        self.item=[]
    def apilar(self,x):
        self.item.append(x)
    def desapilar(self):
        a=self.item.pop()
        return a
    def imprimir (self):
        return (self.item)
    def copiar (self):
        return self.item.copy()
    def ordenar (self):
        return self.item.sort()

p=pila()
suma=0
mediana=0

cantidad=20
cont=0
contmayor=0

for i in range (cantidad):
    p.ordenar()
    c=rn.randint(1,20)
    suma=c+suma
    p.apilar(c)
    if (i==19):
        m=p.copiar()
        mediana=m[10]+m[9]
        






print(m)
print(p.imprimir())
media=suma/cantidad
mediana=mediana/2



print('Esta es la media: ',media)
print('Esta es la mediana',mediana)


moda=0
mayor=m[0]
modas=[]
modamayor=0
for n in m:
    if(n>mayor):
        mayor=n
        cont=0
    if (n==mayor):
        cont=cont+1
        if(cont>=contmayor):
            contmayor=cont
            moda=n
        #    if(moda>modamayor):
         #       modamayor=moda
          #      modas.append(moda)
print('La moda es:',modas)
print('Se repite:', contmayor)





