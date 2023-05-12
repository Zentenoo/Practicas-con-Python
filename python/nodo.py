

class nodo():
    def __init__(self,dato=None):
        self.valor=dato
        self.next=None
    def __str__(self):
        return str(self.valor)


n=nodo(10)
n1=nodo(20)
#print(n)

n.valor=10
n1.valor=20
n2=nodo('Z')


# print('Elemento',n.valor)
# print('Referencia', n.next)

# print('Elemento',n1.valor)
# print('Referencia', n1.next)

n.next=n1

# print('Elemento',n.valor)
# print('Referencia', n.next)

n1.next=n2

# print('Elemento',n1.valor)
# print('Referencia', n1.next)

x=nodo('M')

n.next=x
x.next=n1

# Como lo hizo el profe
# x.next=n.next
# n.next=x


# print('Elemento',n.valor)
# print('Referencia', n.next)


# print('Elemento',x.valor)
# print('Referencia', x.next)

# print('Elemento',n1.valor)
# print('Referencia', n1.next)

# print('Elemento',n2.valor)
# print('Referencia', n2.next)