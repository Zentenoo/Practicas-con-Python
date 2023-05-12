class pila():
    def __init__(self):
        self.item=[]
    def apilar (self,x):
        self.item.append(x)
    def desapilar (self):
        self.item.pop(0)
    def imprimir(self):
        print (self.item)

p= pila()
for i in range (3):
    x=int(input('Ingrese un número: '))
    p.apilar(x)
p.imprimir()
p.desapilar()
p.imprimir()

