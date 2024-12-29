import random
import sys

while True:
    try:
        lvl = int(input("Level: "))
        if lvl <= 0:
            raise ValueError
        break
    except:
        continue

aim = random.randint(1,lvl)

while True:
    try:
        Guess = int(input("Guess: "))
        if lvl <= 0:
            raise ValueError
    except:
        continue
    if Guess == aim:
        print("Just right!")
        sys.exit(0)
    elif Guess > aim:
        print("Too large!")
    else:
        print("Too small!")