def verifica_fermat(a, b, c, n):
    if n != 2 and ((a**n + b**n) == c**n):
        return False

    return True


def testa_teorema(max_num, max_pot):
    n = 2
    while(n <= max_pot):
        # finché n è minore di max_pot ciclo tutte le possibili 
        # permutazioni dei valori a, b e c e testo elevandole a n.
        for i in range(1, max_num + 1):
            for j in range(1, max_num + 1):
                for k in range(1, max_num + 1):
                    if not verifica_fermat(i, j, k, n):
                        print("Ho trovato un controesempio.")
                        return
        # Se non ho trovato un controesempio, che falsifica il teorema,
        # incremento n. Ripeto il test.
        n = n + 1

    print("non ho trovato controesempi")
   
        
testa_teorema(100, 3)
testa_teorema(50, 5)


