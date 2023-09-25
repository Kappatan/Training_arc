def almost_double_factorial(n):
    if n==0:
        return 1
    aaa=1
    for i in range(1,n,2):
        aaa*= i
    return aaa