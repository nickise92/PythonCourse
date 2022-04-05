def terna_corretta(a, b, c):
    return a**2 + b**2 == c**2


def colleziona_terne(max_n):
    risultato = []

    for i in range(2, max_n):
        tmpstr = "("
        if terna_corretta(i-1, i, i+1):
            tmpstr += str(i-1) + "," + str(i) + "," + str(i+1) + ")"
            risultato.append(tmpstr)

    return risultato


print(colleziona_terne(10))
