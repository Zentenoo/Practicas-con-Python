import random as rnd
m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

cont=0
print(' #  T  #S #C')
for t in range (4):
    cc=0
    cs=0
    i=-1
    total=0
    cont=cont+1
    m[t][0]=cont
    while (abs(cc-cs)!=3):
        i+=1
        r1=rnd.random()
        if r1<=0.5:
            cc+=1
        else:
            cs+=1
    m[t][1]=cs+cc
    m[t][2]=cs
    m[t][3]=cc
    print(m[t])









def dibuja(N):
    for a in range(len(N)):
        print ('['),
        for j in range (len(N[a])):
            print ('{:>3s}'.format(str(N[a][j]))),
        print (']')



