def esclamazioni(l):
    newList = []
    for s in l:
        if 'a' in s:
            # se il carattere 'a' è presente
            newList.append("a " + s + "!!!")

    return newList

        
print(esclamazioni(["zebra", "lion", "gorilla", "tiger"]))