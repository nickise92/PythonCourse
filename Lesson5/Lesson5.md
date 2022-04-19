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
print(f.closed)
```
*Output:*
```
[10, -2, 0, 5]
True
```
**Importante:** nel caso del `with`, anche se `l` viene dichiarata all'interno del blocco, non viene 'distrutta' ma 'sopravvive' ed è utilizzabile anche in seguito.

## Exceptions 
Gli errori che avvengono durante l'esecuzione del codice vengono chiamati **eccezioni**. <br>
In molte situazioni, per esempio quando gestiamo gli input, non possiamo essere certi che tutti i dati che vengono letti siano al 100% corretti e coerenti con le nostre specifiche. Possiamo gestire esplicitamente questi errori con l'istruzione `try ... except`.

Il codice prova ad eseguire le istruzioni presenti nel blocco `try`, se qualcosa fallisce, esegue il blocco `except`.
*Esempio*:
```Python
with open('example.txt', 'r') as f:
    l = []
    for line in f:
        try:
            l.append(int(line[:-1]))
        except:
            print('impossibile convertire: "' + line + '"')

print(l)
```
*È importante usare il* `try .. except` *in caso di lettura da file*.

Esiste anche il ramo `finally`: quello che viene scritto in questo blocco viene **sempre** eseguito, è utile per chiudere eventuali file aperti nel caso non si stia utilizzando `with`.
```Python
# Esempio
try:
    f = open('example.txt', 'r')
    # eseguo operazioni sul file
except:
    print("È stata generata un'eccezione")
finally:
    # In questo modo si ha la certezza che il file viene
    # chiuso in ogni caso!
    f.close()

# ...
```

### Sollevare un'eccezione
Le eccezioni vengono generate (o sollevate, da *raise*) quando avviene un errore.

È possibile creare manualmente delle eccezioni, usando l'istruzione `raise`. Per farlo, dobbiamo specificare il tipo di eccezione e il contenuto del messaggio.
```Python
raise ValueError('impossibile convertire')
```
```
Traceback (most recent call last):
  File "main.py", line 14, in <module>
    raise ValueError('impossibile convertire')
ValueError: impossibile convertire
```
Python include già molte [eccezioni](https://docs.python.org/3/library/exceptions.html)

## Funzioni - parametri opzionali
Abbiamo già visto come dichiarare una funzione che richiede dei parametri (detti *argomenti*). È possibile assegnare un valore di default ad un argomento, se la funzione viene chiamata senza assegnare niente usiamo il valore di default.

**Attenzione:** i valori di default vengono valutati una sola volta, meglio evitare oggetti mutabili (come le liste). In questi casi, è buona norma mettere `None` come valore di default e inizializzare il valore in seguito.
```Python
def somma(lista, base = 0):
    for i in lista:
        base += 1
    return base

# Conta partendo da 0
somma([10, 20, 30])
# Conta partendo da 10
somma([10, 20, 30], 10)
```
### Keyword arguments
Quando chiamo una funzione, è possibile esplicitare direttamente i nomi degli argomenti. In questo caso, l'ordine non conta. È molto utile per interagire con funzioni di libreria che hanno molti parametri.

*Esempio*:
```Python
def somma(lista, base = 0):
    for i in lista:
        base += i
    return base

# Passaggio esplicito degli argomenti
somma(base=5, lista=[0, 1, 2, -2])
```

### Tipo del return
In python, il tipo di una variabile non viene specificato, ma viene dedotto dal contesto. Lo stesso vale per il risultato di una funzione: finché la funzione non esegue, non possiamo sapere quale sarà il tipo del risultato.

Il tipo di ritorno può essere eterogeneo, input diversi dello stesso tipo possono darmi risultati di tipo diverso (si pensi alla radice quadrata, che può restituire numeri reali o complessi).

Questa è una feature che può generare più problemi che benfici, va usata con parsimonia. Un caso d'uso valido e comune è, però, quello di ritornare `None` se una funzione fallisce e non riesce a costruire un risultato. <br>
*Esempio*:
```Python
def my_find(lista, valore):
    # Se il find fallisce, ritorna None
    try:
        return lista.find(valore)
    except AttributeError:
        return None

x = my_find([1, 2, 3, 4], 5)
``` 
### Duck typing
Python predilige il *duck typing*. In particolare, non è buona pratica controllare esplicitamente i tipi, meglio usare gli argomenti come si desidera e gestire le eccezioni se le cose non vanno a buon fine.

**Duck Typing:** <br>
*If it looks like a duck, swims like a duck and quacks like a duck, then it is probably a duck!*

### Annotazioni
Indicare il tipo che una funzione si aspetta, tuttavia è molto importante. Questo spesso è parte della documentazione.

Da Python 3.5, è possibile *annotare* argomenti e valore di ritorno di una funzione. Questo non modifica il codice in nessun modo, è solo un suggerimento, ma può essere molto utile per documentare il nostro codice. Inoltre tool esterni, come linter e IDE, possono sfruttare queste informazioni in maniera sistematica.

*Esempio*:
```Python
from typing import List

def somma(lista : List[int], base : int = 0) -> int:
    for i in lista:
        base += i
    return base
```
A livello di sicurezza (del codice), fare controlli di tipo è una cattiva idea, ma ci sono alcuni casi in cui può avere senso lavorare con i tipi. 
