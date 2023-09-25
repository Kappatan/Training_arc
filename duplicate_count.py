

def duplicate_count(text):
    text=text.lower()
    d={}
    l=0
    for c in text:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    if d == {}:
        return 0
    for  n in d.values():
        if n > 1:
            l += 1
    h = max(d.values())
    return len([x for x in d.values() if x==h])