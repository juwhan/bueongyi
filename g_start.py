

#튜플각이다
a = 1,1
b = 2,1
c = 3,1
d = 1,2
e = 2,2
f = 3,2
g = 1,3
h = 2,3
i = 3,3

# 0또는 1로 모양 드러내자
a = [a,1]
b = [b,1]
c = [c,1]
d = [d,1]
e = [e,1]
f = [f,1]
g = [g,1]
h = [h,1]
i = [i,1]

jaryo = [a,b,c,d,e,f,g,h,i]


#(list(tuple))

count = 0

def onclick(a):
    count=0
    count+=1
    x1 = (a[0][0]+1)
    x2 = (a[0][0]-1)
    y1 = (a[0][1]+1)
    y2 = (a[0][1]-1)
    
    n=a[0][0]
    m=a[0][1]

    for i in jaryo:
        if i[0] == (x1,m):
            i[1]+=1
            if i[1]==2:
                i[1]=0
        elif i[0] == (x2,m):
            i[1]+=1
            if i[1]==2:
                i[1]=0
        elif i[0] == (n,y1):
            i[1]+=1
            if i[1]==2:
                i[1]=0
        elif i[0] == (n,y2):
            i[1]+=1
            if i[1]==2:
                i[1]=0    

def value(a):
    value = a[1]
    return

onclick(e)

jaryo1 = [a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1],i[1]]

print(jaryo1)
