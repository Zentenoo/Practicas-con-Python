#Tarea
import GenerarColorRandom as ch
from turtle import*

#color=['green','yellow','red']
w=Screen()
t=Turtle()
cont=0
lado=3
color=[None]*lado
col=ch.colorHexadecimal()
for i in range (lado):
    color[i]=col.retornarcolor()
print(color)
c=0 
for i in range (100):
    cont=cont+1
    if cont==1:
        t.color(color[0])
    if cont==2:
        t.color(color[1])
    if cont==3:
        t.color(color[2])
        cont=0
    t.forward(i)
    t.right(360/lado)
    
