def count_positives_sum_negatives(arr):
    p,n=0,0
    if arr==[]:
        return []
    for i in arr:
        if i>0:
            p+=1
        else:
            n+=i
    return [p,n]