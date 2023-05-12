#Tarea
import GenerarColorRandom as ch
import ClasePilas as pi
from turtle import*
#color=['green','yellow','red','violet','blue','cyan']
w=Screen()
t=Turtle()
cont=0
lado=6
color=[None]*lado

p= pi.pila()
color=ch.colorHexadecimal()

#col=ch.colorHexadecimal()
#for i in range (lado):
#    color[i]=col.retornarcolor()
#print(color)
#c=0
for i in range(lado):
    p.apilar(color.retornarcolor())
print(p.imprimir())
mm=p.copiar
print(p.desapilar())
print(p.desapilar())
print(p.desapilar())
print(p.imprimir())
print(mm())






for i in range (100):
    if cont==lado-1:
        cont=0
    else: cont=cont+1
    t.color(p.desapilar())
    t.forward(i)
    t.right(360/lado)
    
t.penup()
t.goto(-200,150)
t.pendown()
cont=0
for i in range (100):
    if cont==lado-1: cont=0
    else: cont=cont+1
    t.color(color[cont])
    t.circle(50)
    t.right(360/50)

