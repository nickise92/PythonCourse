# Lezione 1 Python

## Materiale di riferimento
1. [Think Python](https://greenteapress.com/thinkpython/html/index.html) (versione in html)
2. [Documentazione ufficiale](https://docs.python.org/3.10/download.html) 
3. Esercizi utili:
   +   [LeetCode](https://leetcode.com/)
   +   [Advent of Code](https://adventofcode.com/)
   +   [Hacker Rank](https://www.hackerrank.com)

## Introduzione
Python è un linguaggio di scripting di alto livello. È interpretato e non compilato, con una sintassi facile e snella (poche parentesi, nessun simbolo di fine riga). Le caratteristiche principali di python sono: <br>
- Linguaggio minimalista: le parentesi vengono usate raramente e l'indentazione ha significato semantico.
- Facile: la sintassi è molto vicina alla lingua (inglese) parlata, uso minimo di *boilerplate*
- Free & Open source
- Alto livello: i dettagliimplementativi sono poco rilevanti. La memoria è gestita in automatico (garbage collection).
- Portabilità: usa bytecode indipendente dall'architettura della CPU.
- Multi-Paradigma: imperativo, funzionale, a oggetti.
- Duck-Typing: il sistema di tipaggio è dinamico.
- Extensible: facile integrare codice scritto in C (o altro)
- Embeddable: facile da integrare in altri software

Inoltre dispone di una grande libreria standard e di un'enorme ecosistema di librerie di terze parti. Le prestazioni sono abbastanza buone perchè sfrutta codice scritto in C.

## Compilazione vs interpretazione
La differenza tra linguaggi compilati e interpretati è particolarmente significativa in caso di errori.
*Esempio*:
<center>
<table>
<tr>
<td style="text-align: center;">C:</td>
<td style="text-align: center;">Python:</td>
</tr>
<tr>
<td>

```C
 #include <stdio.h>
    
int main() {
    printf("Hello, World!");
    printf("%d", 3);
    printf(a);
    return 0;
}
```
</td>
<td>

```Python
print("Hello, World!")
print(3)
print(a)
```
</td>
</tr>
<tr>
<td style="text-align: center;" colspan="2">Errore:</td>
</tr>
<tr>
<td>

```
$ gcc esxample.c
example.c: In function 'main':
example.c:6:12: error: 'a' undeclared (first use in this function)
    6 |     printf(a);
      |            ^  
```
</td>
<td>

```
$ python3 example.py
Hello, World!
3
Traceback (most recent call last):
    File "example.py", line 3, in <module>
      print(a)
NameError: name 'a' is not defined
```
</td>
</tr>
</table>
</center>

**In python vengono eseguite le istruzioni prima dell'errore**.

## Python 2 vs 3
Ci sono alcune differenze sintattiche e semantiche tra le due versioni. Python 2 non è più supportato ufficialmente, ma è ancora possibile trovare del codice python 2.

## Strumenti & Ambienti di sviluppo
È possibile eseguire script python in diversi modi:
1. Tramite la shell python, digitando il comando `python3` in un terminale. (Python deve essere installato sulla macchina). In questo caso si possono iniziare ad eseguire comandi, anche se non è il modo più indicato per eseguire script lunghi e complessi.
2. Editor di testo: qualsiasi editor di testo, da notepad a vim è indicato per scrivere uno script python, basta salvare il file con l'estensione `.py` ed eseguirlo in seguito da un terminale con il comando `python3 <nomeScript>.py`
3. IDE: ambienti di sviluppo adatti che semplificano l'uso di librerie e forniscono numerosi tool extra per facilitare la scrittura degli script.

