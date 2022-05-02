def cripta(text : str, key : int) -> str:
    res = ""
    for c in text:
        # for any char in string 'text'
        if (ord(c) + key) > 122:
            # if the ordinal plus the key is above 122, restart from 'a'
            res += str(chr(ord(c) + key - 25))
        elif (ord(c) + key) > 90 and (ord(c) + key) < 97:
            # if the ordinal plus the key is in [91 .. 96]
            # restart from 'A'
            res += str(chr(ord(c) + key - 25))
        elif c != ' ':
            # if char c is not a space, add the key and save it on the result string
            res += str(chr(ord(c) + key))
        else:
            # if it is a space, put it in the result string
            res += ' '
    # return the res string
    return res

def decripta(text : str, key : int) -> str:
    res = ""
    for c in text:
        # for any char in string 'text'
        if (ord(c) - key) < 65 and ord(c) != 32:
            # if the ordinal plus the key is under 65, go back to 'Z'
            res += str(chr(ord(c) - key + 25))
        elif (ord(c) - key) < 97 and (ord(c) - key) > 90:
            # if the ordinal minus the key is in [91 .. 96] 
            # go back to 'z'
            res += str(chr(ord(c) - key + 25))
        elif c != ' ':
            # if char c is not a space, subtract the key and put it in the string
            res += str(chr(ord(c) - key))
        else:
            # if it is a space, put it in the result string
            res += ' '
    #return the res string
    return res


while True:

    print("Cifrario di Cesare")
    print("Dato un testo ed una chiave, applica il cifrario di Cesare per cifrare il testo")
    print("Scegli l'operazione: ")
    m = int(input("1. Cripta un testo\n2. Decripta un testo\n0. Esci\n>> "))
    if m == 0:
        quit()
    elif m == 1:
        txt = input("Inserisci il testo da codificare: ")
        k = int(input("Inserisci una chiave numerica: "))
        print(f'Testo: "{txt}"\nChiave: {k}\n')
        coded = cripta(txt, k)
        print(f'Testo codificato\n>> "{coded}"\n\n')
    elif m == 2:
        txt = input("Inserisci il testo da decodificare: ")
        k = int(input("Inserisci la chiave numerica: "))
        print(f'Testo: "{txt}";\nChiave: {k}\n')
        decoded = decripta(txt, k)
        print(f'Testo decodificato\n>> "{decoded}"\n\n')
    

