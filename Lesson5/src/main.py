f = open('example.txt', 'r')
lines = f.readlines()
numeri = list()
for l in lines:
    if l == '\n':
        continue
    numeri.append(int(l[:-1]))

print(numeri)
f.close()