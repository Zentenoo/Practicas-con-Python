#Problema 1
# class pila():
#     def __init__(self):
#         self.item=[]
#     def apilar(self,x): 
#         self.item.append(x)
#     def desapilar(self):
#         self.item.pop()
#     def mostrar(self):
#         return self.item
#     def obtener(self):
#         x=self.item.pop()
#         return x
#     def es_vacia(self):
#         return self.item == []

# import re
# numeros=pila()
# signos=pila()
# op=pila()

# operacion=input("Ingrese una operación de suma o resta:")

# num = re.findall('[0-9.0]+', operacion)
# s=re.findall('[+-]+', operacion) 

# for i in range (len(num)):
#     numeros.apilar(num[i])


# for i in range (len(s)):
#     signos.apilar(s[i])
# print('Numeros encontrados: ')
# print(numeros.mostrar())
# print('Signos encontrados: ')
# print(signos.mostrar())

# n1=numeros.obtener() 
# x=len(s)
# resultado=0
# while x>0:
#     n2=numeros.obtener() 
#     sig=signos.obtener()
#     if sig=='-':
#         resultado=resultado-float(n1)
#     else:
#         if sig=='+':
#             resultado=resultado+float(n1)
#     x=x-1
# print('Resultado=', resultado)








#Problema 2

# import random as r

# filas=int(input("Ingrese filas: "))
# columnas=int(input("Ingrese columnas: "))
# matriz=[[r.randint(1,10)for h in range (filas)]for h in range(columnas)]
# print(matriz)

# for i in range (columnas):
#     for j in range (filas):
#         for k in range (columnas):
#             for l in range (filas):
#                 if matriz[i][j]<matriz[k][l]:
#                     apoyo=matriz[i][j]
#                     matriz[i][j]=matriz[k][l]
#                     matriz[k][l]=apoyo

# print(matriz)


########################################Parte 2################################################################


#Problema 1
# num=int(input("Ingrese número de alumnos: "))

# #v=[[input("").capitalize()for i in range (num)]]
# v=[None]*num
# a=[None]*num
# for i in range (num):
#     nombre=input("Ingrese el nombre: ").capitalize()
#     v[i]=nombre
#     apoyo=v[i],":",len(v[i])
#     a[i]=apoyo
# print(v)
# print(a)


#Problema 2

# import random as r
# from random import *


# vector=[]*10
# for i in range(10):
#         ra=r.randint(1,10)
#         vector.append(ra)
# peticion=int(input("Ingrese un número: "))
# posicion=[]
# contador=1
# for i in vector:
#     if(i == peticion):
#         posicion.append(contador)
#     contador=contador+1
# lp=len(posicion)
# if lp>0:
#     print('Tu numero se encuentra en el vector, se repite: ', lp)
#     print('Se encuentra en la posicion: ',posicion)
# else: 
#     print('Mala suerte')
# print(vector)





#Problema 3
# v=[]
# def sumar(V,ele):
#     valor=0
#     for i in range (len(V)):
#         if ele.upper()==V[i]:
#             valor=1
#     return valor
# cadena = input()

# for i in range (len(cadena)):
#     if cadena [i] != ' ' and sumar(v,cadena[i])==0:
#         v.append(cadena[i].upper())
# if cadena!=cadena:
#     print('Chucha')
# else:
#     print(v)

