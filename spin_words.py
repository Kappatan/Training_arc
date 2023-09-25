
def spin_words(sentence):
    k=[]
    sentence=list(sentence.split(' '))
    for i in sentence:
        if len(i)>=5:
            k.append(i[::-1])
        else:
            k.append(i)
    return ' '.join(k)