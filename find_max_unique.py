def find_max_unique(s:str):
    indexes={}
    start=0
    uniq=set([])
    max_arr=''
    for i, s1 in enumerate(s):
        if s1 in uniq:
            max_arr=max(max_arr, s[start:i], key=lambda x:len(x))
            start=indexes[s1]+1
            uniq=set(s[start:i])
        indexes[s1]=i
        uniq.add(s1)
    max_arr = max(max_arr, s[start:], key=lambda x:len(x))
    return len(max_arr)