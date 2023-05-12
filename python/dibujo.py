from turtle import*
w=Screen()
t=Turtle()
lado=int(input("Digite lado: "))
for i in range (36):
    for j in range (lado):
        t.forward(200)
        t.left(360/lado)