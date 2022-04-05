def terna_corretta(a, b, c):
    return a**2 + b**2 == c**2


def colleziona_terne(max_n):
    risultato = []

    for i in range(1, max_n+1):
        for j in range(2, max_n+1):
            for k in range(3, max_n+1):
                if terna_corretta(i, j, k):
                    risultato.append((i, j, k))

    return risultato


print(colleziona_terne(10))
