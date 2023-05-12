
from tkinter import N


class nodo():
    def __init__(self,dato=None,siguiente=None,anterior=None):
        self.valor=dato
        self.next=siguiente
        self.anterior=anterior
    def __str__(self):
        return str(self.valor)



class listaDoble():
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.cantidad=0
    def insertar(self,dato):
        n=nodo(dato)
        if self.cabeza==None:
            self.cabeza=n
            self.cola=self.cabeza
        else:
            n.anterior=self.cola
            self.cola.next=n
            self.cola=n
        self.cantidad+=1
    




