class Nodo:
    dato=None
    refDerecha=None
    refIzquierda=None
    def __init__(self,nuevoDato):
        self.dato=nuevoDato
    def getDato(self):
        return self.dato
    def getRefDerecha(self):
        return self.refDerecha
    def setDato(self,nuevoDato):
        self.dato=nuevoDato
    def setRefDerecha(self,nuevaRef):
        self.refDerecha=nuevaRef
    def getRefIzquierda(self):
        return self.refIzquierda
    def setRefIzquierda(self,nuevaRef):
        self.refIzquierda=nuevaRef

class Lista:
    NodoCabeza=None
    NodoCola=None
    def __init__(self,dato):
        self.NodoCabeza=Nodo(dato)
    def insertarNodo(self,dato):
        if self.listaVacia():
            self.NodoCabeza-Nodo (dato) 
        else:
            nuevoNodo=Nodo (dato)
            nodoFin= self.irAlFinal ()
            nodoFin.setRefDerecha (nuevoNodo)
    def insertarNodoCabeza(self,dato):
        nuevoNodo=Nodo (dato)
        if self.listaVacia():
            self.NodoCabeza=nuevoNodo 
        else:
            nuevoNodo.setRefDerecha(self.NodoCabeza)
            self.NodoCabeza=nuevoNodo
            return True
    def recorrerLista(self):
        if self.listaVacia():
            return False
        else:
            nodoGuia=self.NodoCabeza
            while True:
                print(nodoGuia.getDato(),"->",end="")
                if (nodoGuia.getRefDerecha()!=None):
                    nodoGuia=nodoGuia.getRefDerecha()
                else:
                    break
    def listaVacia(self):
        if self.NodoCabeza==None:
            return True
        else:
            return False
    def irAlFinal(self):
        nodoGuia=self.NodoCabeza
        while True:
            if nodoGuia.getRefDerecha()!=None:
                nodoGuia=nodoGuia.getRefDerecha()
            else:
                return nodoGuia

class Cola(Lista):
    def __init__(self, dato):
        Lista.__init__(self,dato)
        self.tamaño=1
    def insertar(self, dato):
        respuesta=self.insertarNodo(dato)
        if respuesta!=False:
            self.tamaño = self.tamaño + 1
            return respuesta
    def quitar(self):
        dato=self.eliminarNodoCabeza()
        if dato:
            self.tamaño=self.tamaño-1
            return dato 
        else:
            return False

class grafos:
    arreglo=[]    
    def agregarVector(self,dato):
        lista=Lista(dato)
        self.arreglo.append(lista)
    def mostrarVectores(self):
        for lista in self.arreglo:
            lista.recorrerLista()
            print("\n")
    def relacionar(self,vector1,vector2):
        for lista in self.arreglo:
            if lista.NodoCabeza.dato==vector1:
                lista.insertarNodo(vector2)


               
grafo=grafos()

grafo.agregarVector("A")
grafo.agregarVector("B")
grafo.agregarVector("C")
grafo.agregarVector("D")
grafo.agregarVector("E")
grafo.agregarVector("F")

grafo.relacionar("A","E")
grafo.relacionar("B","F")
grafo.relacionar("C","F")
grafo.relacionar("E","B")
grafo.relacionar("E","D")
grafo.relacionar("F","A")

grafo.mostrarVectores()
