
from collections import Counter
import random

import sys

def update_successor_map(window, successor_map, ngram) -> dict:
    if ngram == 2:
        if len(window) == 2:
            if window[0] not in successor_map:
                successor_map[window[0]] = [window[1]]
            else:
                successor_map[window[0]].append(window[1])
            window.pop(0)
    else:
        if len(window) == ngram:
            key = tuple(window[:-1])
            value = window[-1]
            if key not in successor_map:
                successor_map[key] = [value]
            else:
                successor_map[key].append(value)
            window.pop(0)


    return successor_map

def print_examples(successor_map, ngram):

    seed_words1 = ['romeo', 'and', 'juliet', 'by', 'william', 'shakespeare']
    seed_words2 = ['thus', 'with', 'a', 'kiss', 'i', 'die']
    seed_words3 = ['o', 'romeo', 'romeo', 'wherefore', 'art', 'thou']
    seed_words4 = ['a', 'pair', 'of', 'star-crossed', 'lovers', 'take']
    seed_words5 = ['in', 'fair', 'verona', 'where', 'we', 'lay']
    words = seed_words2[:ngram-1]

    print("WORDS: ", words)

    if ngram == 2:
        if words[0] in successor_map:
            print("SUCCESSOR MAP: ", successor_map[words[0]])
            print("WEIGHTED CHOICE: ", random.choice(successor_map[words[0]]))
    elif ngram >= 3:
        key = tuple(words)
        if key in successor_map:
            print("SUCCESSOR MAP: ", successor_map[key])
            print("WEIGHTED CHOICE: ", random.choice(successor_map[key]))
        else:
            print("Key not found")

    print("------------------")
    for i in range(50):
        print(words[0], end=' ')
        if ngram == 2:
            next_word = random.choice(successor_map[words[0]])
            words[0] = next_word
        elif ngram >= 3:
            key = tuple(words)
            if key in successor_map:
                next_word = random.choice(successor_map[key])
                words.pop(0)
                words.append(next_word)
    print("\n----------------")

def main():

    if len(sys.argv) > 1:
        ngram = int(sys.argv[1])
    else:
        ngram = 2

    filename = 'data/romeoandjuliet.txt'
    reader = open(filename)
    lines = reader.readlines()
    reader.close()
    
    punctuation = '.;,-“’”:?—‘!()_[]='

    successor_map = {}
    window = []

    for line in lines:
        words = line.split()
        for word in line.split():
            cleaned_word = word.strip(punctuation).lower()
            window.append(cleaned_word)

            successor_map = update_successor_map(window, successor_map, ngram)



    print_examples(successor_map, ngram)

if __name__ == "__main__":
    main()