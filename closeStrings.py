def closeStrings(word1: str, word2: str) -> bool:
    dict = {}
    for i in word1:
        dict[i] = word1.count(i)
    print(dict)
    for i in word2:
        if i in dict:
            dict[i]-=1
        else:
            return False
    return  any(map(lambda x: x == 0, dict.values())), dict