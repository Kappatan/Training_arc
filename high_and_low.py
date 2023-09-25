def high_and_low(numbers):
    k=list(numbers.split(' '))
    k=[int(x) for x in k]
    return  str(max(k))+' '+str(min((k)))