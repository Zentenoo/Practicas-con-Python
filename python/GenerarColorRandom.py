import random as rn
#from random import*

class colorHexadecimal():
    def __init__(self):
        self.color=None
    def generarValor(self):
        c=rn.randint(15,255)
        m=None
        cc=''
        while c>0:
            m=c%16
            if m==10: m='A'
            if m==11: m='B'
            if m==12: m='C'
            if m==13: m='D'
            if m==14: m='E'
            if m==15: m='F'
            c=c//16
            cc=str(cc)+str(m)
        return (str(cc))
    def retornarcolor(self):
        self.color= '#'+self.generarValor()+self.generarValor()+self.generarValor()
        return self.color
#**************
h=colorHexadecimal()
#print(h.retornarcolor())
