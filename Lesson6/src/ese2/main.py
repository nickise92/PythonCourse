# Exercise 2 Lesson 6

def invert_dict(d : dict()):
    keysList = []
    itemsList = []
    for k, i in d.items():
        if k not in keysList:
            keysList.append(k)
            itemsList.append(i)
    
    inverse = dict()

    for item in itemsList:
        inverse[item] = keysList[item - 1]
    return inverse 

numeri = {'uno':1, 'due':2, 'tre':3}

inverseNum = invert_dict(numeri)
print(inverseNum)
