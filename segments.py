
def segments(x):
    beg=[]
    a=[]
    b=[]
    k=0
    for i in range(len(x)):
        beg += x[i].split('-')
        a.append(beg[i+i])
        b.append(beg[i+i+1])
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    for j in range(7):
        print(j, a)
        if j in a:
            print (j,k)
            k=j
    return x,a,b,k, j