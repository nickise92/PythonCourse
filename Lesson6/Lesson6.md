# Lezione 6 Python

## Stringhe in python

Abbiamo già visto molte variabili di tipo stringa, contengono al loro interno del testo, e sono immutabili. Possiamo pensare alle stringhe come *liste di caratteri*.

```Python
nome = 'Pippo'
for char in nome:
    print(char, end=',')
```
*Output*:
```
P,i,p,p,o,
```

Possiamo usare molte delle operazioni per le liste anche sulle stringhe (e.g., slicing, `in`, `len()`, `find(x)`, `[x]`, ...)

Le stringhe hanno molti metodi personalizzati:
`isalhpa()`, `isdigit()`, `islower()`, `isupper()`, `isspace()`, ...

[Lista completa dei metodi per le stringe](https://docs.python.org/3/library/stdtypes.html).

### Stringhe - join & split
Due metodi molto usati, quando si lavora con le stringhe, sono `join()` e `split()`.
+ Con `' '.join(...)` posso unire più elementi in un unica stringa. Il contenuto della stringa su cui chiamo il metodo è il separatore (e.g. `','.join(...)` per stampare parole separate da virgola).
+ Con `split()` posso spezzare una stringa complessa in una lista di stringhe. Devo specificare il valore che fa da separatore.

*Esempi*:
```Python
l = ['nome', 'cognome', 'matricola']
print(','.join(l))

u = 'Mario,Rossi,VR123456'
print(u.split(','))
```
*Output*:
```
nome,cognome,matricola
['Mario', 'Rossi', 'VR123456']
```

### Stringhe - metodo format
Possiamo costruire stringhe complesse che incorporano dati e valori usando `format()`.

Il metodo prende una stringa con dei "buchi" (indicati con un {}) e li sostituisce con dei valori. I valori vengono presi in ordine, oppure posso specificare la loro posizione (con {0], {1}, ...) oppure usare keyword arguments (`'{x}'.format(x = 10)`). <br>
*Esempio*:
```Python
x = 2
y = 4
print('La somma di {} e {} fa {}'.format(x, y, x+y))
print('La somma di {1} e {0} fa {2}'.format(x, y, x+y))
print('La somma di {x} e {y} fa {res}'.format(x=x, y=y, res=x+y))
```
*Output*:
```
La somma di 2 e 4 fa 6
La somma di 4 e 2 fa 6
La somma di 2 e 4 fa 6
```
### Opzioni Format
Possiamo anche specificare delle opzioni all'interno delle parentesi graffe per stampare il valore secondo determinati criteri.

```Python
data = [1.39312, 36.843002, 127]
# stampa solo le prime due cifre
print('{:.2f}'.format(data[0]))
# occupa 10 caratteri, allinea a destra
print('{:>10}'.format(data[1]))
# stampa i valori della lista
print('|{:>8.2f}|{:>8.2f}|{:>8.2f}'.format(*data))
```
*L'asterisco davanti alla lista la spezza e la rende una serie di argomenti per `format`* 

*Output*:
```
1.39
 36.843002
|    1.39|   36.84|  127.00
```

[Lista completa delle opzioni di `format`](https://docs.python.org/3/library/string.html)

### Formatted string literals
Python 3.6 ha aggiunto un nuovo modo di gestire la formattazione, i formatted string literals (o f-string). Questi snelliscono ed estendono i metodi forniti da `.format()`.

Identifico le stringhe con una f davanti al corpo, posso mettere il nome di variabili (ma anche vere espressioni) dentro il {}.

```Python
x = 2
y = 4
print(f'La somma di {x} e {y} fa {x+y}')
```
*Output*:
```
La somma di 2 e 4 fa 6
```
Posso usare le stesse opzioni di format (e.g. `{:.2f}`, ...).

Un estensione è l'opzione '=', stampa nome e valore di una variabile.
```Python
x = 2
y = 4
print(f'{x=}, {y=}')
```
*Output*:
```
x=2, y=4
```

### Formattazione in stile C
Esiste un metodo più vecchio di formattare stringhe, basato su C.

Meno usato degli altri metodi, ma ancora presente. È più semplice e limitato, ma anche leggermente più veloce in casi semplici.

Devo specificare il tipo dei valori (d per decimali, f per float, s per stringhe, ...) e collegare i valori con % e una tupla

```Python
x = 2
y = 4
print('La somma di %d e %d fa %d' % (x, y, x+y))
```
*Output*:
```
La somma di 2 e 4 fa 6
```

### Librerie utili
Spesso dobbiamo gestire stringhe scritte in formati speciali (json, csv, xml, ...).

Python offre una ricca lista di librerie built-in per gestire questi formati.

+ `import [json]` per gestire [*json*](https://docs.python.org/3/library/json.html).
+ `import [csv]` per gestire [*comma separated values*](https://docs.python.org/3/library/csv.html)
+ `import [xml]` (in particolare ElementTree) per gestire file [*xml*](https://docs.python.org/3/library/xml.html)
+ Un altra libreria molto utile è [*pickle*](https://docs.python.org/3/library/pickle.html), che serve a serializzare codice python.

## Esercitazione
### Esercizio 1: `Lesson6/src/ese1/main.py`
Nel gioco "indovina il numero" il computer sceglie un numero segreto da 1 a 100 (inclusi), e l'utente deve indovinare il numero nel minor numero di tentativi possibili. Il gioco deve fornire un prompt all'utente per inserire il numero, e si deve assicurare che l'input sia valido (ovvero deve essere un numero da 1 a 100). In caso di input invalido, il gioco deve chiedere un nuovo numero, senza generare errori. Il gioco termina quando il numero inserito è uguale al numero segreto. Se il numero inserito è più basso del numero segreto il sistema deve informare l'utente stampando 'troppo basso', se il numero è troppo alto, il sistema deve stampare 'troppo alto'.

Il gioco deve anche tenere traccia del numero di tentativi usati prima di vincere (escludendo casi di input invalido). In caso di vittoria, il programma stampa un numero di tentativi necessari.

### Esercizio 2: `Lesson6/src/ese2/main.py`
Implementare una funzione `invert_dict(d)` che prende un dizionario *d* e costruisce un nuovo dizionario invertito *d'*, ovvero un dizionario che per ogni coppia chiave-valore di *d* continene una coppia valore-chiave, in cui la chiave originale diventa il valore e il valore originale diventa la chiave. Le chiavi di un dizionario sono univoche, mentre i valori non devono esserlo. Se la funzione trova più di una chiave con lo stesso valore, deve sollevare un'eccezione di tipo `ValueError("unique inversion is not possible")`. Per esempio, il dizionario `numeri = {'uno':1, 'due':2, 'tre':3}` verrà trasformato in `{1:'uno', 2:'due', 3:'tre'}`, mentre `gambe = {'uomo' : 2, 'gatto' : 4, 'lampada' : 1, 'cane' : 4}` non può essere invertito (4 dovrebbe puntare sia a gatto che a cane).

Implementare poi il metodo `invert_dict_multi(d)` che opera nello stesso modo di `invert_dict(d)`, ma puntando a una lista di chiavi, invece che a una singola chiave. Quindi se più di una chiave punta allo stesso elemento non sollevo eccezioni. Per esempio, `gambe = {'uomo' : 2, 'gatto' : 4, 'lampada' : 1, 'cane' : 4}` deve costruire il dizionario invertito `{2: ['uomo'], 4: ['gatto', 'cane'], 1 : ['lampada']}`.

### Esercizio 3: `Lesson6/src/ese3/main.py`

Il [cifrario di Cesare](https://en.wikipedia.org/wiki/Caesar_cipher) è un noto e semplice algoritmo crittografico. L'algoritmo prende una stringa e una chiave (un numero n), e sposta tutti i caratteri della stringa di n posizioni nell'alfabeto. Se uno spostamento supera la 'z', si ricomincia a contare dalla 'a'. Per esempio, la stringa **abz**  e la chiave **2** genera la stringa cifrata **cbd**.

Implementare le funzioni `cripta(test, chiave)` che cripta un testo usando il cifrario di Cesare, e la funzione `decripta(testo, chiave)` che fa l'operazione inversa. Assumete che le stringhe contengano solo caratteri (maiuscoli e minuscoli) e spazi. Gli spazi non devono essere cambiati, mentre i caratteri devono essere spostati (rispettando maiuscole e minuscole).

In python, ogni carattere è identificato da un numero intero. Si può ottenere il numero corrispondente utilizzando la funzione `ord('a')`, che può essere utile per trasformare le lettere in numeri e implementare il cifrario. La funzione `chr(n)` fa l'operazione inversa, trasforma numeri in caratteri.

### Esercizio 4: `Lesson6/src/ese4/main.py`

Il file `experiment_data.csv` contiene i risultati di un esperimento. I dati sono raccolti in tre colonne, e i valori sono separati da virgole. Ogni riga rappresenta il risultato di un esperimento, fatta eccezione per la prima riga, che contiene il nome delle colonne (*misure, potenza, guadagno*). La prima colonna contiene numeri interi, mentre le altre due contengono numeri reali.

Implementare una funzione `carica_esperimento(nome_file)` che riceve il nome di un file e ritorna tre liste, la prima conterrà tutti i valori della colonna *misure* (come interi), la seconda tutti i valori della colonna *potenza* (come float), la terza tutti i valori della colonna *guadagno* (come float).

Scrivere poi una funzione `media(l)` e `mediana(l)` che ritornano rispettivamente la [media aritmetica](https://en.wikipedia.org/wiki/Mean) e la [mediana](https://en.wikipedia.org/wiki/Median) di una lista di numeri `l`, e usare queste funzioni per calcolare e stampare a schermo media e mediana di *potenza* e *guadagno*.

Costruire poi due dizionari. Il primo mappa ogni possibile valore della colonna *misure* (un valore intero da 35 a 45) alla lista di valori di *potenza* associati a quel numero di misure effettuate. Il secondo crea un mapping simile, ma per i valori di *guadagno*. Calcolare infine la potenza media e il guadagno medio per ogni valore di misura.
