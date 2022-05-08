# Lezione 8 Python

## Moduli

Python è un linguaggio "battery included", ovvero viene fornito insieme a una ricca raccolta
di **pacchetti e moduli**: librerie software che possono essere importate per facilitare il lavoro.

In genere, si usa `import` per importare un modulo, ma esistono delle varianti.

Un pacchetto è una raccolta di moduli. Si può pensare al pacchetto come ad una cartella, e ai suoi
moduli come ai file contenuti nella cartella (anche se non è sempre cosi).

*Esempio*:
```Python
# importa il modulo
import math
# devo esplicitare il modulo
print(math.p1)

# importa solo un elemento
from math import pi
# posso usare l'elemento importato direttamente
print(pi)

# m è un alias di math
import math as m
print(m.pi)
```
*Output*:
```
3.141592653589793
3.141592653589793
3.141592653589793
```
*Un modo ulteriore per importare, ma è sconsigliato, è quello di importare tutto
il contenuto di una libreria*:
```Python
from math import *
```

### Creare un modulo

Un modulo è un semplice file python. Può essere importato usando il suo nome ed
omettendo l'estensione `.py`.

*Esempio*:
File `my_module.py`

```Python
def somma_1(x):
    return x + 1
```
File `main.py`
```Python
import my_module

print(my_module.somma_1(5))
```
*Output*:

```
6
```
Il modulo creato deve essere nella stessa cartella del file all'interno del quale
viene importato.

### Main

È Possibile definire un `main` del modulo, usando
```Python
if __name__ == '__main__'
```
ovvero una sezione di codice che viene eseguita solo se il codice viene usato direttamente.

Se il modulo viene importato, il codice in 'main' non viene eseguito.

*Aggiungiamo un main al file `my_module.py`*

```Python
def somma_1(x):
    return x + 1

def main():
    print('ciao')
    print(somma_1(41))

if __name__ == '__main__':
    main()
```

In questo caso se eseguo lo script direttamente chiamando l'interpreter sul file `my_module.py`
ottengo come output:
```
python3 my_module.python
ciao
42
```
Mentre se importo il file in un nuovo scritp, ad esempio `test.py`:
```Python
import my_module

print(my_module.somma_1(41))
```
La chiamata della funzione di `my_module` non fa eseguire il `main()`:
```
python3 test.py
42
```

## Ambienti virtuali - venv

È facile installare una libreria, ma in genere si vuole tenere il progetto separato dal resto 
del sistema. Questo ha diversi benefici:

+ È possibile specificare esattamente la versione di python da usare
+ È possibile usare una versione specifica di una libreria (diversa per ogni progetto)
+ È possibile rendere il nostro ambiente di lavoro facilmente riproducibile da altri

Questa cosa è possibile ottenerla crando un **ambiente virtuale**, una "bolla" che separa
il nostro progetto dal resto del sistea.

Python offre un ambiente virtuale di default, **venv**, ma ce ne sono altri (virtualenv, conda, ...)

Documentazione: [venv](https://docs.python.org/3/library/venv.html)

#### Creare un virtual environment su linux

```
python3 -m venv <nome_ambiente>

```
Dopo la creazione dell'ambiente apparirà una nuova cartella `<nome_ambiente>`, che al 
suo interno conterrà una serie di file e cartelle.
```
bin  include  lib  lib64  pyvenv.cfg  share
```
Per **attivare** l'ambiente devo usare il comando
```
source bin/activate
```
A questo punto l'ambiente è attivo e all'inizio della riga di comando sarà presente
il nome dell'ambiente.
```
(nome_ambiente) jarvis@JARVIS:pts/2─(18:06:06 on main ✹ ✭)──> 
```

#### Package manager pip

Utilizzando il comando `python -m pip install <nome_pacchetto>` è possibile installare
pacchetti, se questo comando viene eseguito all'interno del venv creato, automaticamente
saranno installati i pacchetti inerenti alla versione di python corrispondente al venv.

Per rendere l'ambiente facilmente riproducibile è possibile usare il comando
`python -m pip freeze > requirements.txt`, in questo modo tutte le librerie installate
nel venv creato, vengono salvate in un file di testo ed è possibile ricreare in seguito 
l'ambiente usando il comando `python -m pip install -r requirements.txt`.

## NumPy - Numerical Python

Il primo modulo che vedremo è **NumPy**, serve per svolgere computazioni numeriche pesanti.

Questo pacchetto fa da base a molte librerie scientifiche del Python, è quindi importante 
conoscerne i principali elementi. 

NumPy offre la struttura dato "array", che può essere usata per rappresentare array ad
n dimensioni.

Offre inoltre diverse operazioni vettorizzate (i.e., estremamente efficienti). Il codice
è implementato in **C**.

Documentazione: [NumPy](https://numpy.org/doc/stable/)

### NumPy array

A differenza delle liste Python, in NumPy tutti gli elementi di un array devono avere lo
stesso tipo. Quando vengono dichiarati, va fornita una forma (shape) che viene usata da 
numpy per allocare in maniera efficiente i dati.

```Python
import numpy as np

# array di 10 elementi posti a zero
v = np.zeros(10)
print(v)
print(type(v), v.dtype, v.shape)
```
*Output*:
```
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
<class 'numpy.ndarray'> float64 (10, )
```

