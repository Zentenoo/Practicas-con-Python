class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.valor=data
    def __str__(self):
        return str(self.valor)
    def insert (self,data):
        if self.valor:
            if data < self.valor:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif data>self.valor:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.valor=data
    def buscarDato (self,data):
        if data <self.valor:
            if self.left is None:
                print(str(data)+": No existe")
                return (str(data))
            return self.right.buscarDato(data)
        elif data>self.valor:
            if self.right is None:
                print (str(data)+": No existe")
                return (str(data))
            return self.right.buscarDato(data)
        else:
            print(str(self.valor)+": Existe")   
    def printArbol(self):
        if self.left:
            self.left.printArbol()
        print(self.valor)
        if self.right:
            self.right.printArbol()



def ordenarArbol(node,x):
    if node:
        x.insert(node.valor)
        ordenarArbol(node.left, x)
        ordenarArbol(node.right, x)
            
def preorder(node):
    if node:
        print(node.valor,end="-")
        preorder(node.left)
        preorder(node.right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.valor,end="-")
        inorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.valor,end="-")

a=node(45)
a.left=node(100)
a.left.left=node(20)
a.left.right=node(50)
a.right=node(80)
a.right.left=node(10)
a.right.right=node(48)

a.printArbol()
print("Ordenado: ")
y=node(None) #nodo nuevo para llenar los datos
ordenarArbol(a,y)
y.printArbol() 

# r= node(30)
# r.insert(80)
# r.insert(25)
# r.insert(15)
# r.insert(28)
# r.insert(45)
# r.printArbol()
# r.buscarDato(90)

        