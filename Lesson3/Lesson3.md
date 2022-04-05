# Lezione 3 Python

## Istruzioni condizionali: if - else

+ L'istruzione `if` viene utilizzata per verificare una condizione, se è vera viene eseguito un blocco, altrimenti un altro blocco.
+ La clausola `else` è opzionale
+ In python delimitiamo la condizione con `:`, blocco `if` e blocco `else` sono allo stesso livello d'indentazione

*Esempio 1*:
```Python
attivo = True
premium = False

if attivo:
    print("l'utente è attivo")

if premium: 
    print("l'utente è premium")
else:
    print("l'utente non è premium")
```
*Output*:
```
l'utente è attivo
l'utente non è premium
```
*Esempio 2*:
```Python
voto = 17
if voto >= 18:
    print("complimenti")
    print("promosso")
else:
    print("bocciato")

# condizione con liste 
l1 = [1, 2, 3]
l2 = []
l3 = [1, 3, 2]
l4 = l3

# in questo modo si verifica se la lista contiene qualcosa
if l1:
    print("ok")
else:
    print("no")

if l2:
    print("ok")
else:
    print("no")

# l'ordine degli elementi conta, in questo caso l'output è 'no'
if l1 == l3:
    print("si")
else:
    print("no")
```

**If inline o ternario**:
```Python
x = -10
# ..
abx_x = x
if x < 0:
    abx_x = -x
# può essere scritto come
abs_x = x if x > 0 else -x
```

## Ciclo while
Il while ci permette di ripetere più volte un blocco d'istruzioni più volte.
A ogni *ciclo* testiamo il valore di un'espressione e ci fermiamo quando diventa **falsa**

*Esempio*:
```Python
i = 0
while i < 10:
    print(i)
    i = i + 1
```

In alcuni casi devo poter verificare delle condizioni all'interno del while stesso, per poi decidere se continuare o uscire dal ciclo.


**Break**

*Esempio*: data una lista si vuole trovare l'elemento 6
```Python

l = [1, 2, 6, 10, 100, -10, 42]

i = 0

while i < len(l):
    if l[i] == 6:
        print('trovato')
        break
    i += 1 # i = i + 1

# <-- break salta qui
```
**Continue**


```Python
i = 0
somma = 0
while i < len(l):
    if l[i] <= 0:
        i += 1
        continue # salta al ciclo successivo se l[i] è negativo

    # conti...
    somma += l[i]
    i += 1
print(somma)
```

**While - else**
```Python
l1 = []
l2 = []

i = 0
while 1 < len(l1):
    j = 0
    while j < len(l2):
        if l1[i] * l2[j] == 100:
            print('trovato')
            break
        j += 1
    else:
        i + = 1
        continue
    break
```