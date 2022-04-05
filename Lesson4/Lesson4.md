# Lezione 4 Python

## Operazioni su liste

Alcuni esempi:
```Python
l = [0, 1, 2, 3, 4]
print(l[0])
# Posso usare anche indici negativi:
print(l[-1]) # parte dalla fine!
```
*Output*:
```
0 
4
```
Si possono stampare delle sott-liste nel seguente modo:
```Python
print(l[1:3]) # stampa dall'elemento 1 al 3 escluso
```
*Output*:
```
[1, 2]
```
**Copiare una lista**:
```Python
l = [1, 2, 3]
a = l
b = l[:]
c = l.copy # uguale a l[:]
print(a, b)
print(a is l, b is l)
```
*Output*:
```
[1, 2, 3] [1, 2, 3]
True False
```
**Si può usare il passo negativo per invertire una lista**:
```Python
# prende la lista dal primo all'ultimo elemento e la inverte
print(l[::-1]) 
```
*Output*:
```
[3, 2, 1]
```
**In e not in**:

Un modo rapido per verificare se all'interno di una lista è presente un valore è:
```Python
l = [1, 2, 3, 4]
if 3 in l:
    print("yes")
```
*Output*:
```
yes
```
Analogamente posso verificare se un valore *non* è presente:
```Python
if 6 not in l:
    print("yes")
```
*Output*:
```
yes
```
## List comprehension
In generale la sintassi è:

`newlist = [ <expression> for <item> in <iterable> if <condition> == True ]`

Se uso una lista come iterabile, questa non viene modificata, il risultato sarà una nuova lista.
Ogni elemento generato da expression è unico. Posso usare questo metodo per inizializzare delle liste.

*Esempio*:
```Python

```
## Esercizi

### Esercizio 1 

`src/exercise/newton.py`

Un metodo numerico che si può usare per calcolare, in modo approssimato, la radice quadrata di un numero è il [metodo di newton](https://en.wikipedia.org/wiki/Newton%27s_method). Questo metodo parte da una prima stima della radie e migliora iterativamente il valore, avvicinandosi al risultato. Se vogliamo calcolare la radice quadrata di x, partendo dalla stima *s*, possiamo ottenere una stima migliore *s'* usando la formula:
<center>

$\large s' = \frac{s + \frac{x}{s}}{2}$
</center>
Per esempio, se vogliamo calcolare la radice di 4 partendo dalla stima 4, otteniamo 2,5. Se applichiamo lo stesso metodo (usando 2.5 al posto di 4 come stima) otteniamo 2.05, un valore sempre più vicino al valore vero (2).

Scrivere la funzione `migliora_stima(val, stima)`, che implementa la formula del metodo di newton per migliorare (di un passo) la stima dalla radice del numero val. Esso deve ritornare il valore migliorato della stima. Implementare poi la funzione `newton(val, stima)`, che prende un valore e una stima, e continua ad applicare `migliora_stima` finché la differenza tra due passi di miglioramento è , 0.0001. La funzione deve infine ritornare questa stima della radice.

### Esercizio 2  
`src/exercise/fermat.py`

Vogliamo indagare la validità dell'[ultimo teorema di fermat](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem). Esso afferma che, dati tre numeri interi positivi *a*, *b*, *c* e un numero intero *n* maggiore o uguale a 2, l'espressione
<center>

$\large a^n + b^n = c^n$
</center>

può essere vera se e solo se *n* è uguale a 2. Scrivere una funzione `verifica_fermat(a, b, c, b)` che verifica la validità del teorema in una data istanza. Questa funzione deve ritornare `True` se il teorema vale, o `False` altrimenti.

Scrivere il metodo `testa_teorema(max_num, max_pot)` che serve a testare il teorema più volte. Esso deve usare `verifica_fermat` per ogni combinazione di *a*, *b*, *c* con i numeri compresi tra 1 e `max_num`, e li deve testare provando tutte le potenze comprese tra 2 e `max_pot`. Notate che `max_num` e `max_pot` devono essere inclusi nella ricerca. Per esempio, `testa_teorema(3, 3)` proverà a mettere 1, 2, 3 in *a*, *b*, *c* (in tutte le combinazini possibili (1,1,1,), (1,1,2), ... ); proverà queste combinazioni usando $n = 2$ e $n = 3$. Se `testa_teorema` trova un caso in cui `verifica_fermat` è falso, esso deve stampare "ho trovato un controesempio" e fermarsi. Se invece alla fine di tutto non ha trovato nessun controesempio, esso deve stampare "non ho trovato controesempi".

### Esercizio 3

`src/exercise/pitagora.py`

Una tripletta di numeri che soddisfa il teorema quando $n = 2$ è nota come terna pitagorica. Per esempio, (3, 4, 5) è una terna pitagorica corretta, perché $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.
Scrivere una funzione `terna_corretta(a, b, c)` che ritorni `True` se *a, b, c* sono una terna pitagorica. Notare che l'ordine è importante, confronto sempre la somma delle potenze dei primi due elementi con la potenza del terzo elemento.

Implementare poi la funzione `colleziona_terne(max_n)`. Questa funzione ritorna una lista di tuple che sono terne pitagoriche. Essa testa tutte le terne (*a, b, c*) instanziate con tutte le possibili combinazioni di valori tra 1 e `max_n` (incluso). Usare la funzione `terna_corretta(a, b, c)` per identificare quali combinazioni vanno aggiunge alla collezione. Per esempio, `colleziona_terne(10)` ritorna la lista `[(3, 4, 5), (4, 3, 5), (6, 8, 10), (8, 6, 10)]`.

### Esercizio 4

`src/exercise/nested.py`

Implementare la funzione `nested_sum(1)`. Essa riceve in input una lista di liste di numeri interi *l* e deve calcolare la somma di tutti i numeri presenti nelle liste contenute in `l`. Per esempio, `nested_sum([[1,2,3], [5], [-1 , -1, -1]])` deve ritornare il valore 8.

Implementare la funzione `nested_compact(l)`. Essa riceve in input una lista di liste di numeri interi *l* e deve costruire una nuova lista che contiene i numeri di *l*, ma senza ripetizioni. L'ordine dei numeri deve essere preservato, se un numero appare più volte, solo la prima occorrenza deve essere inserita nella lista finale. Per esempio, `nested_compact([[1, 2, 3], [-1, 3], [-2, -2]])` deve ritornare la lista `[1, 2, 3, -1, -2]`.

### Esercizio 5

`src/exercise/esclamations.py`

Scrivere una funzione `esclamazioni(l)` che riceve una lista di stringhe e ritorna una nuova lista che segue i seguenti parametri:
1. Se una stringa non contiene il carattere `a` deve essere ignorata;
2. Le stringhe che contengono il carattere `a` devono essere modificate, aggiungendo la stringa "a" prima della stringa originale, e la stringa "!!!" alla fine;
3. La lista finale deve essere ordinata in ordine alfabetico.

Per esempio, `esclamazioni(["zebra", ,"lion", "gorilla", "tiger"])` deve ritornare la lista `["a gorilla!!!", "a zebra!!!"]`

