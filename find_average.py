def find_average(numbers):
    k=0
    if len(numbers) == 0:
        return 0
    else:
        for i in range(0, len(numbers)):
            k+=numbers[i]
        return k/len(numbers)