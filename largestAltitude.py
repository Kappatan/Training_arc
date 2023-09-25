
def largestAltitude ( gain) -> int:
    d=0
    k=0
    for i in range (len(gain)):
        d+=gain[i]
        if d>k:
            k=d
    return k