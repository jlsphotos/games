import random

num = random.randint(1, 100)
counter = 0
guess = -1


def header():
    print("----------------------------------")
    print("        Guess Number")
    print("----------------------------------")
    print()

def how_close(g, n):
    num = abs(g - n)
    if (num > 5) and (num < 10):
        print('Getting close!!!!!!')
    elif num < 5:
        print('Almost on it')
    else:
        pass

header()

while guess != num:
    guess = int(input('have a guess: '))
    how_close(guess, num)
    counter += 1
    if guess < num:
        print('Too low!')
    elif guess > num:
        print('Too High')
    else:
        print('bingo, you took {} attempts to guess the number {}'.format(counter,num))
