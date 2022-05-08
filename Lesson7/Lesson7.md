# Lezione 7 Python

## Concetti di Programmazione ad Oggetti (OOP)

La *programmazione a oggett (OOP)* è un paradigma che si basa sull'idea di **classi**: tipi personalizzati definiti da un programmatore per raccogliere e organizzare codice e dati. <br>
L'OOP è un topic enorme. Nel corso ne vedremo solo una piccola parte, principalmente legata all'uso di classi e oggetti già pronti.

Definiamo:
+ **Classe:** un tipo. In python tutto è una classe, compresi i tipi builtin.
+ **Oggetto (o istanza):** un elemento di una classe. Per esempio, 5 è un oggetto della classe `int`, 'ciao' è oggetto/istanza della classe `str` .

### Classi

Possiamo definire una **classe** nel seguente modo:
```Python
class Punto:
""" Rappresenta un punto in un piano bidimensionale """
```

Possiamo definire un **oggetto** della nostra classe. I dati al suo interno si chiamano **attributi della classe**.
```Python
p = Punto()
p.x = 5.0
p.y = 6.0
print(f"{p.x = }, {p.y = }")
```
*Output*:
```
p.x = 5.0, p.y = 6.0
```
**N.B.**: a differenza del Java o di altri linguaggi con tipaggio statico, non dobbiamo necessariamente definire gli elementi che stanno all'interno di una classe (ma è buona cosa farlo)

Le nostre classi creano oggetti **mutabili**, è possibile modificare i valori contenuti all'interno.<br>
Passare un oggetto della classe a una funzione passa l'elemento stesso, non una sua copia.
*Esempio*:
```Python
q = Punto()
q.x = 1
q.y = 2
print(f"{q.x = }, {q.y = }")

def sposta(punto):
    punto.x += 1
    punto.y += 1

# q viene modificato.
sposta(q)
print(f"{q.x =}, {q.y = }")
```
*Output*:
```
q.x = 1, q.y = 2
q.x = 2, q.y = 3
```

Per fare una copia, è possibile importare il modulo `copy` e usare `copy()` (per copie superficiali) oppure `deepcopy()` (per copie profonde).

```Python
import copy

a = Punto()
a.x, a.y = 0

c = a
print(f"({a.x} {a.y}) == ({c.x} {c.y}), {c is a}")

d = copy.copy(a)
print(f"({a.x} {a.y}) == ({d.x} {d.y}), {d is a}")
```
*Output*:
```
(2 2) == (2 2), True
(2 2) == (2 2), False
```
*Differenza tra `copy` e `deepcopy`*
```Python
class Segment:
    """ Rappresenta il segmento che passa dal punto inizio al punto fine """


r = Segment()
r.inizio = Punto()
r.inizio.x, r.inizio.y = 0, 0
r.fine = Punto()
r.fine.x, r.fine.y = 5, 2
print(f"da {r.inizio.x, r.inizio.y} a {r.fine.x, r.fine.y}")


# copia con assegnamento
r2 = r
print(r is r2, r.inizio is r2.inizio)
# copia superficiale: 
# r ed r3 non sono la stessa cosa, ma r.inizio 
# ed r3.inizio sono la stessa cosa
r3 = copy.copy(r)
print(r is r3, r.inizio is r3.inizio)
# copia con 'deepcopy'
# in questo caso r ed r4 sono due cose diverse ma ora
# anche r.inizio e r4.inizio sono due elementi separati
r4 = copy.deepcopy(r)
print(r is r4, r.inzio is r4.inizio)
```

### Metodi
Le classi non definiscono solo il contenuto (in termini di dati) di un tipo, ma anche il loro **comportamento**. Una funzione interna alla classe si chiama **metodo**, il primo elemento è sempre un riferimento alla classe stessa. Posso usare un metodo con la sintassi `oggett.metodo(...)`.

*Esempio*:
```Python
class Time:
    """ Rappresenta l'ora del giorno 
        
        Attributi: hour, minute, second
    """
    def print_time(self):
        print(f"{self.hour}:{self.minute}:{self.second}")

time = Time()
time.hour = 11
time.minute = 59
time.second = 30
time.print_time()
```
*Output*:
```
11:59:30
```
### Magic methods
Esistono dei metodi speciali, chiamati **magic methods** o **dunders** (*double underscore*) che permettono alla classe di comportarsi in modo speciale.

I più comuni sono `__init__` e `__str__`, usati per inizializzare e convertire in stringhe rispettivamente.

Possono anche implementare molto altro, per esempio il supporto all'operatore `+`.

#### `__init__` & `__str__`
Riprendendo l'esempio della classe Time, definiamo i due metodi.
```Python
class Time:
    """ Rappresenta l'ora del giorno
        Attributi: hour, minute, second.
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __add__(self, other):
        if isinstance(other, int):
            return self.add_seconds(other)
        elif isinstance(other, Time):
            return self.add_time(other)
        else:
            raise ValueError("unsupported operation")

    def add_time(self, time):
        self.second += time.second
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        self.minute += time.minute
        if self.minute >= 60:
            self.minute -= 60
            self.houre += 1
        self.hour += time.hour
        return self
```
Il metodo `__init__` ci permette di scrivere nel seguente modo:
```Python
start = Time(11, 54, 36)
elapsed = Time(1, 04, 11)
```
Questo è da considerare come se si scrivesse:
```Python
start = Time.__init__(11, 54, 36)
# lo stesso vale per 'elapsed'

# proseguendo il codice
start = start + elapsed     # somma due Time()
start += 90                 # aggiunge a start 90 secondi
print(start)                # richiama il metodo __str__
```
*Indagare come è strutturata una classe*:
```Python
print(dir(start)) # ritorna una lista di tutto il contenuto della classe a cui appartiene 'start'
print('-' * 40)
print(vars(start)) # ritorna un dizionario con all'interno le variabili della classe di 'start'
```
*Output*:
```
['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add_seconds', 'add_time', 'hour', 'minute', 'second']
---------------------------------------
{'hour': 12, 'minute': 58, 'second': 47}
```

### Inheritance - (ereditarietà)
Python supporta il meccanismo dell'*ereditarietà*, che permette di derivare nuove classi a partire da quelle già definite realizzando una gerarchia di classi.

La classe eredita tutti i metodi dalla classe padre, e può aggiungerne di nuovi (o specializzare quelli esistenti).

*Esempio*:
```Python
class Father():
    """ classe padre """

class Son(Father):
    """ classe figlio, eredita da Father """

p = Father()
f = Son()
print(isinstance(p, Son), isinstance(f, Padre))
```
*Output*:
```
False, True
```
Python supporta l'ereditarietà multipla, ovvero una classe può da più classi genitori.

### Iteratori

Python usa un meccasnismo basato su **iteratori** per scorrere oggetti che rappresentano collezioni finite di altri oggetti.

Per esempio, possiamo scorrere una `list` usando un iteratore con `iter()`.

Il meccanismo degli iteratori fa da base a molte delle features che abbiamo visto, come ad esempio le `slice`, `zip`, `enumearte`, `items()`, ecc...

Per implementarlo, vanno implementati i metodi `__iter__()` e `__next__()`.

*Esempio*:
```Python
l = [ i for i in range(10)]

# uso esplicito dell'iteratore
for i in iter(l):
    print(i)

# uso implicito, ma identico
for i in l:
    print(i)
```

### Generatori

Il concetto di iteratore si può estendere con l'uso dei generatori: delle funzioni che producono nuovi elementi in maniera sequenziale.

I generatori sono più potenti degli iteratori, possono generare un numero potenzialmente infinito di elementi.

L'istruzione `yield` generalizza il return. Ritorna il valore e salva la posizione, richiamare il generatore fa ripartire dallo stesso punto.

*Esempio*:
```Python
def my_range(n):
    """ Versione semplificata di range """

    i = 0
    while i < n:
        yield i
        i += 1

for i in my_range(10):
    print(i, end=',')
```
*Output*:
```
0,1,2,3,4,5,6,7,8,9,
```
*Tutte le istruzioni usate nella list comprehension*
```Python
l = [i*2 for i in range(10)] # sto usando un generatore.
print(type(i*2 for i in range(10)))
print(l)
```
*Output*:
```
<class 'generator'>
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### Le funzioni sono oggetti

In python, anche le funzioni sono oggetti.

È possibile salvare una funzione in una variabile, passarla come argomento ad un'altra funzione, ecc.

Questa feature permette a python di supportare anche il paradigma della **programmazione funzionale**.

*Esempio*:
```Python
def raddoppia(x):
    return x * 2

l = [i for i in range(1, 6)]
l = list(map(raddoppia, l))
print(l)
```
*Output*:
```
[2, 4, 6, 8, 10]
```

### Decoratori

I decoratori sono funzioni che prendono come input altre funzioni, servono ad "arricchire" una funzione.

Sono funzioni che prendono e ritornano una funzione, arricchendola in qualche modo.

Per usarli, uso la sinstassi:

```Python
@decoratore
def funzione...
```

*Esempio*:

*Immaginiamo di avere del codice che lavora correttamente ma che impiega molto tempo ad essere eseguito, se si volesse fare un controllo di quanto tempo impiegano le varie funzioni, si dovrebbe scrivere un timer per ogni funzione, che inizia prima di chiamarla e termina alla fine della funzione. Queste aggiunt "sporcano" il codice, possiamo usare i decoratori per ovviare questo problema.*

```Python
from time import time

def timer(func):
    # stampa il tempo di esecuzione di una funzione
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__} executed in {(t2 - t1):.4f}s')
        return result
    return wrap_func

@timer
def somma(n):
    res = 0 
    for i in range(n):
        res += i
    return res

somma(10)
somma(10000000)
```
*Output*:
```
Function somma executed in 0.0000s
Function somma executed in 0.4754s
```
Alcuni casi d'uso dei decoratori possono essere:
+ creare un timer
+ creare un logger
+ decoratore `attribute` in ambito OOP
