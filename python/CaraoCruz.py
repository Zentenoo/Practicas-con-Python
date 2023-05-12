import random as rdn

dim=int(input("Digite la dimensión del vector: "))
v=[None]*dim
contC=0
contS=0
porcent=0
for i in range (0,dim):
    valorRand=rdn.randint(0,10000)
    if valorRand%2:
        v[i]="C"
        contC=contC+1
    else:
        v[i]="S"
        contS=contS+1

porcentC=(contC*100)/dim
porcentS=(contS*100)/dim
print (v)
print ("Salieron ",contC, "caras, con porcentaje de ",porcentC,"%")
print ("Y ", contS, "sellos con porcentaje de ",porcentS,"%")


#Como lo hizo el profe


import random as rnd
d=int(input('Dimensión del arreglo: '))
m=[0]*d
contC=0
contS=0
porcent=0
for i in range (d):
    r1=rnd.random()
    if r1<=0.5:
        m[i]="C"
        contC=contC+1
    else:
        m[i]="S"
        contS=contS+1
porcentC=(contC*100)/d
porcentS=(contS*100)/d
print (m)
print ("Salieron ",contC, "caras, con porcentaje de ",porcentC,"%")
print ("Y ", contS, "sellos con porcentaje de ",porcentS,"%")


d=50
n=[None]*d
cc=0
cs=0
i=-1
while (cc-cs!=3):
    i+=1
    r1=rnd.random()
    if r1<=0.5:
        n[i]="C"
        cc+=1
    else:
        n[i]="S"
        cs+=1

print (n)
print('CC= ',cc)
print ('CS= ',cs)
    





