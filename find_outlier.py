def find_outlier(integers):
    k=0
    for i in range(3):
        if integers[i]%2==0:
           k+=1
        else:
            k-=1
    if k>0:
        for i in range(len(integers)):
            if integers[i] % 2 == 1:
                return integers[i]
    elif k<-0:
        for i in range(len(integers)):
            if integers[i] % 2 == 0:
                return integers[i]