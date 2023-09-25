def duplicate_encode(word):
    char_count = {}
    w=word.lower()
    r=''
    for i in w:
        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i]=1
    for i in w:
        if char_count[i]>1:
            r+=')'
        else:
            r+='('
    return r