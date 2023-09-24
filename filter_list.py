def filter_list(l):
    m=[]
    for i in range (len(l)):
        if isinstance(l[i], int) is True:
            m.append(l[i])
            return m