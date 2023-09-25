def uniqueOccurrences(arr: List[int]) -> bool:
    dict = {}
    for i in arr:
        dict[i] = arr.count(i)
    return len(dict.values()) == len(set(dict.values()))