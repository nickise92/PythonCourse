testo = 'testo di esempio'
contatore = dict()
for carattere in testo:
    if carattere in contatore:
        contatore[carattere] += 1
    else:
        contatore[carattere] = 1

print(contatore)

