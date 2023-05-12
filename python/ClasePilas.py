import GenerarColorRandom as ch

class pila():
    def __init__(self):
        self.item=[]
    def apilar (self,x):
        self.item.append(x)
    def desapilar (self):
        a= self.item.pop()
        return a
    def imprimir(self):
        return (self.item)
    def copiar (self):
        return self.item.copy()

p= pila()
color=ch.colorHexadecimal()
#for i in range (3):
x=color.retornarcolor()
p.apilar(x)

#p.desapilar()
#print(p.imprimir())
#print(p.desapilar())
#print(p.imprimir())


