def tribonacci(signature, n):
    for i in range(n-3):
        signature.append(sum(signature[0+i:3+i]))
    return signature