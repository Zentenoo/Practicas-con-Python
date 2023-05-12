class Vertice(object):
  def __init__(self, n):
    self.nombre = n
    self.vecinos = list()
  def agregarVecino(self, v):
    if v not in self.vecinos:
      self.vecinos.append(v)
      self.vecinos.sort()


class Grafo(object):
  vertices = {}
  def agregarVertice(self, vertice):
    if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
      self.vertices[vertice.nombre] = vertice
      return True
    else:
      return False
  def agregarBorde(self, u, v):
    if u in self.vertices and v in self.vertices:
      self.vertices[u].agregarVecino(v)
      self.vertices[v].agregarVecino(u)
      return True
    else:
      return False   
  def printGrafo(self):
    for key in sorted(list(self.vertices.keys())):
      print(key + str(self.vertices[key].vecinos))



g = Grafo()
a = Vertice('A')
b = Vertice('B')
c = Vertice('C')
d = Vertice('D')
e = Vertice('E')
f = Vertice('F')
for i in range(ord('A'), ord('G')):
  g.agregarVertice(Vertice(chr(i)))
  
bordes = ['AB','AE','AF','BA','BD','BE','DB','DE','EA','EB','ED','EF','FA','FE']

for borde in bordes:
  g.agregarBorde(borde[:1],borde[1:])

g.printGrafo()