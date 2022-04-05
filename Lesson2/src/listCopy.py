import time

start = time.time()
l2 = []
for i in range(10000):
    # Ricopia la lista ad ogni iterazione, aggiungendo un nuovo elemento i-esimo
    l2 = l2 + [i]

end = time.time()

print(len(l2), end - start)
