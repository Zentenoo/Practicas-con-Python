class suma():
    def __init__(self, pvalora=None, pvalorb=None):
        self.a = pvalora
        self.b = pvalorb
        self.r = None
    def sumar(self):
        self.r = self.a + self.b
    def resultado(self):
        return self.r

#***********Llamando a la clase SUMA
operacion = suma()
operacion.a=2
operacion.b=3
operacion.sumar()
print(operacion.resultado())

        
    
