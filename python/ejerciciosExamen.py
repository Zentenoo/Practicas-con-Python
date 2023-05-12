# def crearArreglo ():
#     tamaño=int(input("Ingrese el tamaño del arreglo: "))
#     arreglo=[None]*tamaño
#     for i in range(tamaño):
#         arreglo[i]=int(input("Ingrese un número: "))
#     print(arreglo)
#     sumarPares(arreglo=arreglo)
# def sumarPares(arreglo):
#     sumas=[]
#     suma=0
#     for i in arreglo:
#         cont=2
#         if cont>0:
#             if i%2==0:
#                 suma=suma+i
#                 cont=cont-1
#         sumas.append(suma)
#         suma=0
#         print(sumas)

# crearArreglo()


from random import*
def CargarDatos(dim):
    x=[None]*dim
    for i in range(i+1):
        x[i]=randint(1,10)
    return x
#Método forma inicial
def BuscarPar1(nums,valor):
    sw=0
    c=0
    for i in range(len(nums)-1):
        for j in range (i+1,len(nums)):
            c+=1
            if nums[i] + nums[j]==valor:
                print('Par Encontrado',(nums[i],nums[j]))
                sw=1
    print(c)
    if sw==0:
        print('No existen pares')
#Método 2 Ordenando Datos
def BuscarPar2(nums,valor):
    sw=0
    nums.sort()
    print(nums)
    (inicio,fin)=(0,len(nums)-1)
    while inicio<fin:
        c+=1
        if nums[inicio]+nums[fin]==valor:
            print('Par Encontrado',(nums[inicio],nums[fin]))
            sw=1
        if nums[inicio]+nums[fin]<valor:
            inicio=inicio+1
        else:
            fin=fin-1
    print(c)
    if sw==0:
        print('No tiene Pares')
    
#Llamando métodos
if __name__=='__main__':
    A=CargarDatos(2)
    print(A)
    suma=10
    print("Método 1")
    BuscarPar1(A,suma)
    print("Método 2")
    BuscarPar2(A,suma)