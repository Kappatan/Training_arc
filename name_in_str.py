
def name_in_str(str, name):
    k=0
    name=name.lower()
    for i in str.lower():
        if i==name[k] :
            k+=1
            if k==len(name):
                return True
    return False
