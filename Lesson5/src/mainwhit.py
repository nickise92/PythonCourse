# In questo modo il file viene chiuso dopo la fine di with

with open('example.txt', 'r') as f:
    l = []
    for line in f:
        if line != '\n':
            l.append(int(line[:-1]))

print(l)