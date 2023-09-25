
def decodeString(s) :
    i=0
    while i <(len(s)):
        if s[i]==']':
            k=i
            while s[k]!='[':
                k-=1
            m=k-1
            while s[m].isnumeric():
                m-=1
            m+=1
            l=int(s[m:k])
            s=s[:m]+(l*s[k+1:i])+s[i+1:]
            i=-1
        i+=1
    return s