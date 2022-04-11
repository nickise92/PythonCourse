# Lezione 5 Python

## Dizionari ("mappe")
Le liste sono strutture dato utili, ma poco flessibili:
+ Dobbiamo usare numeri per indicizzare.
+ Gli indici partono sempre da 0 e sono contigui.

Per superare queste limitazioni possiamo usare un **dizionario**. <br>
Un dizionario mappa ogni chiave ad un valore, la chiave può essere di qualsiasi tipo immutabile. È efficiente (hash table) e mutabile (come le liste).

*Esempio*:
```Python
# dichiarazione di un dizionario
d1 = {}
d2 = dict()
# stampa il dizionario
print(d1, d2) 
```
*Esempio di dizionario*
```Python
# mappa parole italiane in parole inglesi
ita2eng = dict()

ita2eng['ciao'] = 'hello'
print(ita2eng)
print(ita2eng['ciao'])

ita2eng['gatto'] = 'cat'
print(ita2eng)
print(ita2eng['gatto'])

ita2eng['cane'] = 'dog'
print(ita2eng)
print(ita2eng['cane'])
```
*Output*:
```
{'ciao':'hello'}
hello
{'ciao':'hello', 'gatto':'cat'}
cat
{'ciao':'hello', 'gatto':'cat','cane':'dog'}
dog
```

Il dizionario non garantisce che gli elementi inseriti al suo interno mantengano l'ordine in cui sono stati inseriti. Gli elementi all'interno di un dizionario vengono chiamate **coppie chiave-valore**

**Alcune proprietà**
La chiave deve essere *immutabile* mentre il valore no. Le chiavi possono avere *tipo eterogeneo* e sono *univoche*.

```Python
# Valido
l = [1, 2, 3]
ita2eng['uno', 'due', 'tre'] = l
```
*Errore!*
```Python
# NON Valido
ita2eng[l] = 'one, two, three'
# La lista non è 'hashable'
```

```
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    ita2eng[l] = 'one, two, three'
TypeError: unashable type: 'list'
```

I dizionari forniscono un'interfaccia simile a list (e.g, in, len(), clear(), copy(), ...). Non possiamo però modificare direttamente l'ordine degli elementi (`insert(val, pos)`, `sort()`). L'ordine è gestito dalla funzione hash (una funzione che facilita la ricerca delle chiavi nel dizionario). Possiamo usare cicli `for` per iterare tutti i *valori*. Se vogliamo iterare solo le chiavi, o le coppie chiave valore, usiamo rispettivamente i metodi `keys()` e `items()`.
```Python
# Esempio:
for el in ita2eng:
    # Stampa le chiavi
    print(el)

for ita, eng in ita2eng.items():
    # Stampa parola italiana e inglese
    print(ita, eng)

# Per iterare esplicitamente le chiavi
for key in ita2eng.keys():
    print(key)
```
*Outputs*:
```
ciao
gatto
cane
ciao hello
gatto cat
cane dog
ciao 
gatto
cane
```

### Varianti: collections
Il modulo *collections*

```Python
from collection import Counter

c = Counter('testo di esempio')
print(c)
```
*Output*:
```
Counter({'e': 3, 't': 2, 's': 2, 'o': 2, ' ': 2, 'i': 2, 'd': 1, 'm': 1, 'p': 1})
```
Immaginiamo di voler fare la stessa cosa ma senza utilizzare il metodo `Counter`
```Python
testo = "testo di esempio"
contatore = dict()
for carattere in testo:
    if carattere in contatore:
        contatore[carattere] += 1
    else:
        contatore[carattere] = 1

print(contatore)
```
*Output*:
```
{'t': 2, 'e': 3, 's': 2, 'o': 2, ' ': 2, 'd': 1, 'i': 2, 'm': 1, 'p': 1}
```

## Input 

### Linea di comando

Fin'ora, abbiamo usato solo dati inseriti manualmente nel codice, ma spesso non è un buon modo di opeare. Possiamo acquisire dati da diverse fonti: linea di comando, file, internet, ... <br>
Per acquisire direttamente un valore, usiamo la funzione `input()`.
```Python
# Esempio di input da linea di comando
n = input("Inserisci nome: ")
print(n)
type(n)
```
*Output*:
```
inserisci nome: Nick
Nick
<class 'str'>
```
Il valore è **sempre letto come stringa**, se si vuole ottenere altro, dobbiamo convertirlo `int()`, `float()`, `bool()`, ...

*Esempio: dato un numero stamparlo incrementato di 2*
```Python
n = int(input("Inserisci un numero: "))
print(n + 2)
```
*Output*:
```
Inserisci un numero: 10
12
```
### File
Possiamo aprire un file con `open(<name>, <args>)`
args:
  + 'r' apre in sola lettura (valore di default se viene passato un solo argomento)
  + 'w' apre in scrittura (cancella il contenuto, se il file esiste)
  + 'a' appende contenuto al file esistente
  + 'r+' lettura e scrittura

Quando abbiamo finito di lavorare con il file, dobbiamo chiuderlo `f.close()`.

Il metodo `f.read()` ritorna il file come unica stringa, mentre `f.readline()` legge una riga. `f.readlines()` ritorna una lista di stringe (una stringa per riga). In alternativa, si può usare il `for`.

Si possono usare `write()` e `writeline()` per scrivere.

*Esempio*:
```Python
# Apre il file in sola lettura
f = open('example.txt', 'r')
lines = f.readlines()
numeri = list()
for l in lines:
    if l == '\n':
        continue
    numeri.append(int(l[:-1]))

print(numeri)
f.close()
```
*Output*:
```
[10, -2, 0, 5]
```
Nella lettura dei file è importante ricordare che con la funzione `readline()` viene spostato avanti un cursore ad ogni chiamata, quindi verrà letta ad ogni chiamata una riga successiva.

### Input - with
Aprire e chiudere un file è un'operazione comune, ma soggetta ad errori. Python mette a disposizione un costrutto comodo per automatizzare questa operazione, il `with`
*Esempio*:
```Python
# In questo modo il file viene chiuso dopo la fine di with

with open('example.txt', 'r') as f:
    l = []
    for line in f:
        if line != '\n':
            l.append(int(line[:-1]))

print(l)
```




