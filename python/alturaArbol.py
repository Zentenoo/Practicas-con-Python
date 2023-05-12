def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.left), altura(nodo.right))

def numNodos(node):
    if node is None:
        return 0
    else:
        return 1+numNodos(node.left)+numNodos(node.right)