# abc=[None]*27 #97  #241ñ
cba=[None]*27 #65  #209Ñ

# letras=97
letrasMas=65

# for i in range (27):
#     if i==14:
#         abc[i]=chr(241)
#     else:
#         abc[i]=chr(letras)
#         letras=letras+1
# print(abc)

for i in range (27):
    if i==14:
        cba[i]=chr(209)
    else:
        cba[i]=chr(letrasMas)
        letrasMas=letrasMas+1
print(cba)

def oracion(ora):
    letras=[]
    ora=ora.upper()
    for i in range(len(ora)): 
        letras.append(ora[i])
    cifrar(letras=letras)
def cifrar(letras):
    oraCifr=''
    l=letras
    cifrado=['']*len(l)
    for i in range(len(l)):
        for t in range(27):
            if l[i]=='X':
                cifrado[i]=cba[0]
            elif l[i]=='Y':
                cifrado[i]=cba[1]
            elif l[i]=='Z':
                cifrado[i]=cba[2]
            else:
                if l[i]==cba[t]:
                        cifrado[i]=cba[t+3]
                elif l[i]==" ":
                    cifrado[i]=" "
    for i in range(len(cifrado)):
        oraCifr=oraCifr+cifrado[i]
    descifrar(oraCifr,cifrado)

def descifrar(oraC,letrasE):
    oraDesCifr=''
    l=letrasE
    descifrado=['']*len(l)
    for i in range(len(l)):
        for t in range(27):
            if l[i]=='A':
                descifrado[i]=cba[24]
            elif l[i]=='B':
                descifrado[i]=cba[25]
            elif l[i]=='C':
                descifrado[i]=cba[26]
            else:
                if l[i]==cba[t]:
                        descifrado[i]=cba[t-3]
                elif l[i]==" ":
                    descifrado[i]=" "
    for i in range(len(descifrado)):
        oraDesCifr=oraDesCifr+descifrado[i]
    imprimir(oraDesCifr, oraC)
def imprimir(fraseOriginal,fraseEncriptada):
    print(fraseOriginal)
    print(fraseEncriptada)    

oracion(input("Ingrese frase: "))
# ora=input("Escriba una oracion: ").upper()
# final=""

    
# for i in range (len(ora)):
#     for t in range (len(cba)):
#         if ora[i]==cba[t]:
#             if cba[t]=="X":
#                 final+=cba[0]
#             elif cba[t]=="Y":
#                 final+=cba[1]
#             elif cba[t]=="Z":
#                 final+=cba[2]
#             else:
#                 final+=cba[t+3]
# print(final)
# desci=input("Escriba una oracion: ").upper()
# final2=""
# for i in range (len(desci)):
#     for t in range (len(cba)):
#         if desci[i]==cba[t]:
#             if cba[t]=="A":
#                 final2+=cba[24]
#             elif cba[t]=="B":
#                 final2+=cba[25]
#             elif cba[t]=="C":
#                 final2+=cba[26]
#             else:
#                 final2+=cba[t-3]

# print(final2)

