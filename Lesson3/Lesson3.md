# Lezione 3 Python

## Istruzioni condizionali: `if - else`

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

### If inline o ternario
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


### Break

*Esempio*: data una lista si vuole trovare l'elemento 6
```Python

l = [1, 2, 6, 10, 100, -10, 42]

i = 0

while i < len(l): # finché la posizione è minore dell'elemento 'l'
    if l[i] == 6:
        print('trovato')
        break
    i += 1 # i = i + 1

# <-- break salta qui
```
### Continue


```Python
i = 0
somma = 0
while i < len(l):
    if l[i] <= 0:
        i += 1 # incremento i
        continue # salta al ciclo successivo se l[i] è negativo

    # conti...
    somma += l[i]
    i += 1
print(somma)
```

### While - else

In python è possibilie definire l'else di un ciclo `while`, serve a semplificare un *pattern* molto comune. <br>
Il codice nel ramo else è eseguito solo se non uso mai il break.
*Esempio*:
```Python
piatti = ['pasta', 'pizza', 'risotto']
i = 0
while i < len(piatti):
    if piatti[i] == 'insalata':
        print('un insalata per favore')
        break
    else:
        i += 1
else:
    print("non c'è insalata")
```
Riprendendo l'esempio precedente, se nella lista cercassimo il numero '7' non lo troveremo e non verrebbe stampato nulla a video.
```Python
l = [1, 2, 3, 6, 10, 100, -10, 42, 6]
i = 0
trovato = False

while i < len(l):
    if l[i] == 7:
        trovato = True
        print('trovato!')
        break
    i += 1

if not trovato: 
    print("Il 7 non c'è")
```
Si dovrebbe quindi inserire una variabile (*flag*) booleana per determinare se l'elemento viene trovato. Utilizzando il ramo `else` del `while` si ottiene invece: 
```Python
l = [1, 2, 3, 6, 10, 100, -10, 42, 6]
i = 0

while i < len(l):
    if l[i] == 7:
        print('trovato')
        break
    i += 1
else:
    print("Il 7 non c'è")
```
*Output*:
```
Il 7 non c'è
```

Immaginiamo ora di avere due liste di numeri `l1` ed `l2`. Si vuole determinare se una combinazione di numeri delle due liste fa 100. In questo caso, se venisse inserito un `break` dopo la `print('trovato')`, si uscirebbe dal while più interno, ma non dal while esterno, quindi se nella lista `l1` ci fosse un secondo 10, 'trovato' verrebbe stampato due volte.

```Python
l1 = [1, 4, 6, 10, 8, 6]
l2 = [3, 4, 5, 9, 2, 10, 10]

i = 0

while 1 < len(l1):
    j = 0
    while j < len(l2):
        if l1[i] * l2[j] == 100:
            print('trovato')
        j += 1
    i + = 1
```
Utilizzando il costrutto `else` del `while` otteniamo:
```Python
l1 = [1, 4, 6, 10, 8, 6]
l2 = [3, 4, 5, 9, 2, 10, 10]

i = 0

while 1 < len(l1):
    j = 0
    while j < len(l2):
        if l1[i] * l2[j] == 100:
            print('trovato')
            break # interrompe il ciclo più interno, se non arrivo al break entro nel ramo 'else'
        j += 1
    else: # incremento il contatore del ciclo più esterno e continuo.
        i += 1
        continue
    break # se il viene eseguito il break più interno, l'istruzione successiva è questo break.
```
*Output*:
```
trovato
```
## Ciclo for 
Il ciclo `while` non è l'unico modo di ripetere più volte un blocco di istruzioni. Possiamo usare anche il `for`. In python, il `for` itera su una serie di elementi, in altri linguaggi questo viene chiamato `for each`.

*Esempio*:
```Python
gioco = [1, 2, 3, 'stella']
for fase in gioco:
    print(fase)
```
Inoltre il for può semplificare il codice, non serve gestire gli indici:
```Python
piatti = ['pasta', 'pizza', 'risotto']
for p in piatti:
    if p == 'insalata':
        print("un insalata per favore")
        break
else:
    print("non c'è insalata")
```
Riprendendo l'esempio della lista `l1`, possiamo stamparla utilizzando un ciclo `for`:
```Python
l1 = [1, 2, 3, 6, 10, 100, -10, 42, 6]
for i in l1:
    print(i)
```
*Output*:
```
1
2
3
6
10
100
-10
42
6
```
Un altro esempio di semplificazione del codice utilizzando il `for` è il seguente:
```Python
l = [1, 2, 3, 6, 10, 100, -10, 42, 6]
somma = 0

for i in l:
    if i <= 0:
        continue
    somma += i

print(somma)
```
*Output*:
```
170
```

### `range()` - argomenti
Al metodo `range()` posso passare gli argomenti in tre modi diversi:
1. `range(n)` - Solo il punto di arrivo, in questo caso parte da 0 fino a n-1
2. `range(2, n)` - Specifico il punto di partenza (incluso) e quello di arrivo (escluso)
3. `range(0, n, 2)` - Specifico un "passo", ovvero di quanto incrementare ad ogni ciclo.

### `enumerate()`

Python mette a disposizione un modo per iterare una lista ottenendo posizione e valore degli elementi.
```Python
l = [1, 2, 3, 4]
for pos, val in enumerate(l):
    print(pos, val)
```
*Output*:
```
0, 1
1, 2
2, 3
3, 4
```

### `zip()`
Permette di accedere allo stesso indice di due liste distinte, ad esempio:
```Python
l1 = [1, 4, 6, 10, 8, 10, 6]
l2 = [3, 4, 5, 9, 2, 10, 10]

for x, y in zip(l1, l2):
    print(x, y)
```
*Output*:
```
1 3
4 4
6 5
10 9
8 2
10 10 
6 10
```
È possibile anche utilizzare `enumerate()` e `zip()` assieme:
```Python
l1 = [1, 4, 6, 10, 8, 10, 6]
l2 = [3, 4, 5, 9, 2, 10, 10]

for n, (x, y) in enumerate(zip(l1, l2)):
    print(n, x, y)
```
*L'output sarà composto da posizione, x, y*:
```
0 1 3
1 4 4
2 6 5
3 10 9
4 8 2
5 10 10
6 6 10
```

## Tuple

Alcune delle istruzioni usate precedentemente (`zip`, `enumerate`) costruiscono delle tuple. <br>
In Python, le tuple, come le stringhe, sono sequenze immutabili.

Si usano per gestire collezioni di oggetti che non cambiano nel tempo.

### Dichiarare una tupla:

+ `t1 = (1, 2, 'Ciao', 4)`
+ `t2 = tuple(...)` - dichiarazione esplicita
+ `t3 = (1,)` notare che le tuple con un solo elemento **richiedono la virgola**
+ `t4 = ([1, 3], [1, 4])` - le tuple possono contenere *liste*

**N.B. gli elementi all'interno possono essere mutabili.**

*Esempio*:
```Python
l = [1, 2, 6, 10, 100, -10, 42, 6]
for t in enumerate(l):
    print(t[0], t[1])
```
*Output*:
```
0 1
1 2
2 6
3 10
4 100
5 -10
6 42
7 6
```

### Unpacking
Permette di associare una sorta di referenza agli elementi della tupla. 

*Esempio*
```Python
t = tuple(1, 2, 3, 'ciao', [1, 2, 3])
n1, n2, n3, parola, lista = t
```

### Swap
Utilizzando le tuple si possono scambiare i valori di due variabili

*Approccio classico*:
```Python
a = 5
b = 10
print(a, b)
tmp = a
a = b
b = tmp
print(a, b)
```
*Output*:
```
5 10
10 5
```

Sfruttando le tuple si può eseguire il tutto in una sola riga:

```Python
a = 5
b = 10
print(a, b)
a, b = b, a # sfruttiamo l'unpacking e le tuple
print(a, b)
```
*Output*: 
```
5 10
10 5
```

Le tuple possono essere usate anche per ritornare più valori dalla stessa funzione.
*Esempio*:
```Python
def calcola_media(l):
    # calcoli....
    media = 10
    errore = 0.5
    return media, errore
```

In questo caso, python promuove gli elementi nel return ad una tupla.

Essendo immutabili non ci sono metodi per eliminare/aggiungere elementi. Attenzione che come detto precedentemente ciò che si memorizza sono sempre riferimenti. Se l'elemento è mutabile lo posso modificare, ma non posso far puntare quella particolare locazione della tupla a un altro elemento.
