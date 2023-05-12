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
    def addFinal(self, pdato): #Inserta Nodo al final 
        x=nodo(pdato)
        if self.cantidad==0:
            self.frente=x
        else:
            nActual=self.frente
            while nActual.next!=None:
                nActual=nActual.next
            nActual.next=x
        self.cantidad+=1
    def addMitad(self,pdato,elem):
        x=nodo(pdato)
        if self.cantidad==0:
            self.frente=x
        else:
            nActual=self.frente
            while nActual.next!=None:
                if nActual.valor==elem:
                    x.next=nActual.next
                    nActual.next=x
                nActual=nActual.next
        self.cantidad+=1
    def delNodo (self,elem):
        nActual=self.frente
        if nActual.valor==elem:
            self.frente=nActual.next
            nActual.next=None
        else:
            while nActual.next!=None:
                if nActual.valor==elem:
                    x=nActual.next
                    nActual.next=x.next
                nActual=nActual.next
        self.cantidad-=1
    def imprimir (self): #Mostrar lista
        a=self.frente
        print("")
        while a !=None:
            print (a.valor, end='=>')
            a=a.next

l=lista()


l.addFrente(4)
l.addFrente(3)
l.addFrente(3)
l.addFrente(3)
l.addFrente(1)
l.addFinal(9)
l.addFinal(9)
l.addFinal(9)
l.addFinal(1)
l.addMitad(7,4)
l.delNodo(1)
l.imprimir()