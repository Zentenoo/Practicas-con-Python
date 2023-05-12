import random as rd

class nodo():
    def __init__(self,dato):
        self.valor=dato
        self.left=None
        self.right=None
        self.cantidad=0
    def insertNodo(self,dato):
        if self.valor:
            if dato>=self.valor:
                #derecha
                if self.right is None:
                    self.right=nodo(dato)
                else:
                    self.right.insertNodo(dato)
            else:
                #izquierda
                if self.left is None:
                    self.left= nodo(dato)
                else:
                    self.left.insertNodo(dato)
        else:
            self.valor=dato
        self.cantidad+=1




        
#Lo de abajo es un intento de busqueda
def preorder(node):
    if node:
        print(node.valor,end="-")
        preorder(node.left)
        # if node.valor==4:
        #     cont=cont+1
        preorder(node.right)
#         if node.valor==4:
#             cont=cont+1
# print("El número 4 se repitió",cont, " veces")

def inorder(node):
    if node:
        preorder(node.left)
        print(node.valor,end="-")
        preorder(node.right)

def postorder(node):
    if node:
        preorder(node.left)
        preorder(node.right)
        print(node.valor,end="-")

b=nodo(50)
# b.insertNodo(80)
# b.insertNodo(85)
# b.insertNodo(60)
for i in range (10):
    b.insertNodo(rd.randint(1,5))
preorder(b)
# print("")
# inorder(b)
# print("")
# postorder(b)