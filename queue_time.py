def queue_time(customers, n):
    if customers==[]:
        return 0
    k=[0]*n
    for i in customers:
        mint=min(k)
        min_till_index = k.index(mint)
        k[min_till_index]+=i
    return max(k)