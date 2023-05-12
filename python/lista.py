from nodo import nodo


class lista():
    def __init__(self):
        self.frente=None
        self.cantidad=0
    def addFrente(self, pdato): #Inserta Nodo al frente
        x=nodo(pdato)
        if self.cantidad==0:
            self.frente=x
        else:
            x.next=self.frente
            self.frente=x
        self.cantidad=self.cantidad+1
    def addFinal(self, pdato): #Inserta Nodo al final #no esta acabado
        x=nodo(pdato)
        a=self.cantidad
        while a>0:
            self.frente.next
            print(self.frente)
            a=a-1
        self.final=x
        x.next=self.final
        self.cantidad=self.cantidad+1
    def imprimir (self): #Mostrar lista
        a=self.frente
        print("")
        while a !=None:
            print (a.valor, end='=>')
            a=a.next

l=lista()
l.addFrente(10)
#l.imprimir()
l.addFrente(20)
#l.imprimir()
l.addFrente('M')
l.addFrente('Z')
#l.imprimir()

l.addFinal(20)
l.addFinal(30)

l.imprimir()