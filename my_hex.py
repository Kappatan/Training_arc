def my_hex(a:int):
    k:List[int]=[]
    if a==0:
        return '00'
    elif a>255:
        return 'FF'
    elif a<0:
        return '00'
    while a!=0:
        k.append(a%16)
        a=a//16
        print(k,a)
    for c in range(len(k)):
        if k[c]>9:
            k[c]=chr(55+k[c])
        else:
            k[c]=str(k[c])
        if len(k)==1:
            k.append('0')
    return ''.join(k[::-1])
def rgb(r:int, g:int, b:int)->str:
    return my_hex(r)+my_hex(g)+my_hex(b)