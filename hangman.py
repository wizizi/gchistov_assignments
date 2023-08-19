import random
import re


def play(words):
    n = len(words)
    tries = 6
    word = words[random.randint(0, n - 1)]
    nl = len(word)
    guessed = ['_'] * nl
    while True:
        print(f'Currently guessed: {"".join(guessed)}')
        hits = guess(word)
        if(len(hits) == 0):
            tries -= 1
            print(f'Wrong! Guesses left: {tries}')
            if tries == 0:
                print(f'You lost! The word was {word}')
                return
        elif guessed[hits[0]] == '_':
            nl -= len(hits)
            for i in hits:
                guessed[i] = word[i]
            if nl == 0:
                print(f'You guessed the word {word}!')
                return
            
        

def guess(wrd):
    letter = '#'
    while not re.match('^[a-z]$', letter):
        letter = input('Guess letter: ')
    hits = []
    for i, l in enumerate(wrd):
        if l == letter:
            hits.append(i)
    return hits

    
    


try:
    f = open('words.txt', 'r')
    words = f.read().split()
    while True:
        play(words)
except:
    print("Can't find word list. Create a word list file under the name words.txt")