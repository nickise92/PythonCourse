# Exercise 2 Lesson 6

def invert_dict_multi(d):
    inverse = {}
    keysList = []
    itemsList = []
    new_val = []

    for k in d:
        keysList.append(k)
    
    for i in d:
        itemsList.append(d[i])

    for i in range(len(d)):
        itemsListCpy = itemsList.copy()
        itemsListCpy.pop(itemsListCpy.index(itemsList[i]))
        if itemsList[i] not in itemsListCpy:
            inverse.setdefault(itemsList[i], new_val.append(keysList[i]))
            print(keysList[i])
        else:
            inverse.setdefault(itemsList[i], new_val.append(keysList[i]))
        
    return inverse
            


def invert_dict(d):
    inverse = {}
    keysList = [] 
    itemsList = []
    for k in d:
        keysList.append(k)

    for i in d:
        itemsList.append(d[i])
    
    for i in range(len(d)):
        itemsListCpy = itemsList.copy()
        itemsListCpy.pop(itemsListCpy.index(itemsList[i]))
        if itemsList[i] not in itemsListCpy:
            inverse.setdefault(itemsList[i], keysList[i])
        else:
            raise ValueError("unique inversion is not possible")

    return inverse

numeri = {'uno': 1, 'due': 2, 'tre': 3}
gambe = {'uomo': 2, 'gatto': 4, 'lampada': 1, 'cane': 4}
print(numeri)
inverseNum = invert_dict(numeri)
print(inverseNum)
print('-' * 20)
# part 2
print(gambe)
multipleInversion = invert_dict_multi(gambe)
print(multipleInversion)
print('-' * 20)
# Raise error
inverseGamb = invert_dict(gambe)
print(inverseGamb)
