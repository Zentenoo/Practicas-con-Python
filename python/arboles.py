class nodo():
    def __init__(self,dato):
        self.valor=dato
        self.left=None
        self.right=None

def preorder(node):
    if node:
        print(node.valor,end="-")
        preorder(node.left)
        preorder(node.right)
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
def altura(node):
    if node is None:
        return 0
    return 1 + max(altura(node.left), altura(node.right))

def numNodos(node):
    if node is None:
        return 0
    else:
        return 1+numNodos(node.left)+numNodos(node.right)
#..........................

a=nodo(50) #Nodo Raiz
print(a.left,a.valor,a.right)

ai=nodo(100)
ad=nodo(200)

a.left=ai
a.right=ad
print(a.left.valor,a.valor,a.right.valor)


ad.left=nodo('A')
ad.right=nodo('B')
a.right.left=nodo('A')
a.right.right=nodo('B')
print(a.right.left.valor,a.right.valor,a.right.right.valor)

a.right.left.left=nodo('Z')
print(a.right.left.left.valor,a.right.left.valor)

a.right.left.left.left=nodo(8)
a.right.left.left.right=nodo(9)
print(a.right.left.left.left.valor,a.right.left.left.valor,a.right.left.left.right.valor)

# print("postorder")
# postorder(a)
# print()

# print ("inorder")
# inorder(a)
# print()

# print("preorder")
# preorder(a)

print("altura:",altura(a))


def numNodos(node):
    if node is None:
        return 0
    else:
        return 1+numNodos(node.left)+numNodos(node.right)
print("nodos",numNodos(a))
