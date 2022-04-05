import math


def migliora_stima(val, stima):
    return (stima + (val / stima)) / 2


def newton(val, stima):
    nuova_stima = migliora_stima(val, stima)
    while not stima - nuova_stima < 0.0001:
        # aggiorno il valore della stima con l'ultimo valore calcolato
        stima = nuova_stima
        # eseguo un nuovo miglioramento della stima
        nuova_stima = migliora_stima(val, stima)

    print(nuova_stima)
    return nuova_stima


newton(4, 10)
newton(4, 0.05)
newton(17, 10)
print(math.sqrt(4), math.sqrt(17))