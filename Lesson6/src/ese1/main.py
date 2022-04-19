# Exercise 1, Lesson 6
from random import randint

secret = randint(1, 100)
tries = 0

print("Guess the number!")
num = int(input("What number have I draw? "))
if num != secret:
    flag = True
else: 
    flag = False
    tries += 1
    
while flag:
    if num >= 1 and num <= 100:
        tries += 1
        if num > secret:
            print("Il numero è troppo alto!")
        if num < secret:
            print("Il numero è troppo basso!")
        num = int(input("Ritenta: "))
    else:
        num = int(input("Ritenta: "))
    
    if num == secret:
        flag = False

print("Hai trovato la risposta in " + str(tries) + " tentativi!")
