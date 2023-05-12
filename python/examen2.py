a=['A','B','C','D','E','F','G','H''I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b=input("Digite Frase: ").upper()
S=""

def xyz(n):
    if n <2:
        return n
    else:
        return xyz(n-1) + xyz(n-2)
for i in range (len(b)):
    for j in range(len(a)):
        if b[i]==a[j] and [i]!=" ":
            S+=a[j+xyz(i)]
print(S)