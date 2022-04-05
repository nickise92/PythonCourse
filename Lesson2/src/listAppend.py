import time

start = time.time()
l1 = []
for i in range(10000):
    # Aggiungiamo l'elemento i-esimo alla lista ad ogni iterazione
    l1.append(i)

end = time.time()

print(len(l1), end - start)
