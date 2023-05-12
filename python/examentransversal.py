from random import randint


def a():
    num = []
    mayor=1
    cant = int(input("Ingrese el tamaño de la lista: "))
    for i in range(cant):
        num.append(randint(-10,10))

    find = False
    registrados = []
    mayor3=0
    jmayor=0
    for i in range(cant):
        for j in range(cant):
            if (mayor<(num[j] * num[i]) and not num[j] in registrados):
                if(num[j]>=mayor3 or num[i]>=jmayor):
                    mayor=num[i]*num[j]
                    mayor3=num[i]
                    jmayor=num[j]
                registrados.append(num[i])
                registrados.append(num[j])
                find = True
            
    print("Los pares son: ", mayor3, " y ", jmayor,"la multiplicacion mayor es:", mayor)
    if not find:
        print("No se encontraron pares")
    print(num)

def b():
    num = []
    cant = int(input("Ingrese el tamaño de la lista: "))
    for i in range(cant):
        num.append(randint(1,10))

    n = int(input("Ingrese un valor: "))
    find = False
    registrados = []
    for i in range(cant):
        for j in range(cant):
            for k in range(cant):
                if (n == num[j] + num[i] + num[k] and not 
                    num[j] != num[k] and not num[i]!=num[k] in registrados):
                    print("El trío son: ", num[k],num[j], num[i])
                    registrados.append(num[k])
                    registrados.append(num[j])
                    registrados.append(num[i])
                    find = True
    if not find:
        print("No se encontraron tríos")
    print(num) 

def c():
    num = []
    cant = int(input("Ingrese el tamaño de la lista: "))
    for i in range(cant):
        num.append(randint(1,10))

    n = int(input("Ingrese un valor: "))
    find = False
    registrados = []
    for i in range(cant):
        for j in range(cant):
            if (n == num[j] + num[i] and not (num[j]!=num[i]) in registrados):
                print("Los pares son: ", num[j], " y ", num[i])
                registrados.append(num[i])
                registrados.append(num[j])
                find = True
    if not find:
        print("No se encontraron pares")
    print(num)



# from random import randint
# def a():
#     num = []
#     cant = int(input("Ingrese una cantidad de numeros: "))
#     for i in range(cant):
#         num.append(randint(1,10))

#     n = int(input("Ingrese un valor: "))
#     find = False
#     registrados = []
#     for i in range(cant):
#         for j in range(cant):
#             if (n == num[j] + num[i] and not num[j] in registrados):
#                 print("Los pares son: ", num[j], " y ", num[i])
#                 registrados.append(num[j])
#                 registrados.append(num[i])
#                 find = True
#     if not find:
#         print("No se encontraron pares")
#     print(num)

# def b():
#     num = []
#     cant = int(input("Ingrese una cantidad de numeros: "))
#     for i in range(cant):
#         num.append(randint(1,10))

#     sw = 0
#     c = 0
#     num.sort()

#     print(num)
#     (inicio, fin) = (0, len(num) - 1)
#     while inicio < fin: 


a()