# Lezione 6 Python

## Esercitazione
### Esercizio 1:
Nel gioco "indovina il numero" il computer sceglie un numero segreto da 1 a 100 (inclusi), e l'utente deve indovinare il numero nel minor numero di tentativi possibili. Il gioco deve fornire un prompt all'utente per inserire il numero, e si deve assicurare che l'input sia valido (ovvero deve essere un numero da 1 a 100). In caso di input invalido, il gioco deve chiedere un nuovo numero, senza generare errori. Il gioco termina quando il numero inserito è uguale al numero segreto. Se il numero inserito è più basso del numero segreto il sistema deve informare l'utente stampando 'troppo basso', se il numero è troppo alto, il sistema deve stampare 'troppo alto'.

Il gioco deve anche tenere traccia del numero di tentativi usati prima di vincere (escludendo casi di input invalido). In caso di vittoria, il programma stampa un numero di tentativi necessari.

### Esercizio 2:
Implementare una funzione `invert_dict(d)` che prende un dizionario *d* e costruisce un nuovo dizionario invertito *d'*, ovvero un dizionario che per ogni coppia chiave-valore di *d* continene una coppia valore-chiave, in cui la chiave originale diventa il valore e il valore originale diventa la chiave. Le chiavi di un dizionario sono univoche, mentre i valori non devono esserlo. Se la funzione trova più di una chiave con lo stesso valore, deve sollevare un'eccezione di tipo `ValueError("unique inversion is not possible")`. Per esempio, il dizionario `numeri = {'uno':1, 'due':2, 'tre':3}` verrà trasformato in `{1:'uno', 2:'due', 3:'tre'}`, mentre `gambe = {'uomo' : 2, 'gatto' : 4, 'lampada' : 1, 'cane' : 4}` non può essere invertito (4 dovrebbe puntare sia a gatto che a cane).

Implementare poi il metodo `invert_dict_multi(d)` che opera nello stesso modo di `invert_dict(d)`, ma puntando a una lista di chiavi, invece che a una singola chiave. Quindi se più di una chiave punta allo stesso elemento non sollevo eccezioni. Per esempio, `gambe = {'uomo' : 2, 'gatto' : 4, 'lampada' : 1, 'cane' : 4}` deve costruire il dizionario invertito `{2: ['uomo'], 4: ['gatto', 'cane'], 1 : ['lampada']}`.