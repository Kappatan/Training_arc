
def typist(s):
    u, l = 0, 1
    k=0
    for i in range(len(s)):
        if ord(s[i])<97:
            if u==1:
                k+=1
            else:
                k+=2
                u,l=1,0
        else:
            if l==1:
                k+=1
            else:
                k+=2
                u,l=0,1
    return k
