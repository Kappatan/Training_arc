
def mySqrt(x):
    if x == 0:
        return 0
    left, right = 1, x // 2 + 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1
