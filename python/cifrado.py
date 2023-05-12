abc=[0]*27

#RELLENANDO VECTOR CON FOR
v=65
for i in range(27):
    if i!=14:
        abc[i]=chr(v)
        v=v+1
    if i==14:
        abc[i]=(chr(ord('ñ'))).upper()
    
print(abc)

def obtenerfrase(frase):
    letras=[]
    frase=frase.upper()
    long=len(frase)
    for i in range(long): #OBTENIENDO LETRAS
        letras.append(frase[i])
    encriptarFrase(letras=letras)
def encriptarFrase(letras):
    fraseEncrip=''
    l=letras
    long=len(l)
    letrasEncrip=['']*long
    for i in range(long): #CAMBIANDO FRASE
        for x in range(27):
            if l[i]=='X':
                letrasEncrip[i]=abc[0]
            elif l[i]=='Y':
                letrasEncrip[i]=abc[1]
            elif l[i]=='Z':
                letrasEncrip[i]=abc[2]
            if l[i]!='X' and l[i]!='Y' and l[i]!='Z':
                if l[i]==abc[x]:
                        letrasEncrip[i]=abc[x+3]
                elif l[i]==" ":
                    letrasEncrip[i]=" "
    longF=len(letrasEncrip)
    for i in range(longF):
        fraseEncrip=fraseEncrip+letrasEncrip[i]
    desEncriptarFrase(fraseEncrip,letrasEncrip)

def desEncriptarFrase(fraseE,letrasE):
    fraseDesEncrip=''
    l=letrasE
    long=len(l)
    letrasDesEncrip=['']*long
    for i in range(long): #DESENCRIPTANDO FRASE
        for x in range(27):
            if l[i]=='A':
                letrasDesEncrip[i]=abc[24]
            elif l[i]=='B':
                letrasDesEncrip[i]=abc[25]
            elif l[i]=='C':
                letrasDesEncrip[i]=abc[26]
            if l[i]!='A' and l[i]!='B' and l[i]!='C':
                if l[i]==abc[x]:
                        letrasDesEncrip[i]=abc[x-3]
                elif l[i]==" ":
                    letrasDesEncrip[i]=" "
    longF=len(letrasDesEncrip)
    for i in range(longF):
        fraseDesEncrip=fraseDesEncrip+letrasDesEncrip[i]
    imprimir(fraseDesEncrip, fraseE) #IMPRIMIENDO FRASE

def imprimir(fraseOriginal,fraseEncriptada):
    print("-----------------------------------------------------------------------")
    print("FRASE ORIGINAL: ",fraseOriginal)
    print("FRASE ENCRIPTADA: ", fraseEncriptada)
    print("-----------------------------------------------------------------------")

print('-----------------------------------------------------------------------------------------------------------------------------')
resp=input("Ingrese 1 para iniciar el programa: ")
while resp=='1':
    frase=input('Coloca tu frase: ')
    obtenerfrase(frase)
    resp=input("¿Escribir otra frase? |1=si|0=no|: ")
    if resp!='1' and resp!='0':
        while resp!='1' and resp!='0':
            print("Intente de nuevo xnx")
            resp=input("¿Escribir otro nombre? |1=si|0=no|: ")
print('-----------------------------------------------------------------------------------------------------------------------------')
print("Adiós vuelve prontooo! nxn")