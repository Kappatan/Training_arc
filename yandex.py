def ya(s):
    r=len(s)-1
    l=0
    k=[]
    while s:
        if s[l]**2> s[r]**2:
            k.insert(0,s[l]**2)
            s.pop(0)
            r-=1
        else:
            k.insert(0,s[r]**2)
            s.pop(r)
            r-=1
    return k