
from collections import Counter
import random

import sys


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

            # if len(window) == 2:
            #     if window[0] not in successor_map:
            #         successor_map[window[0]] = [window[1]]
            #     else:
            #         successor_map[window[0]].append(window[1])
            #     window.pop(0)

            if len(window) == 3:
                key = (window[0], window[1])
                value = window[2]
                if key not in successor_map:
                    successor_map[key] = [value]
                else:
                    successor_map[key].append(value)
                window.pop(0)


    # random.seed(1)

    # print(successor_map['romeo']) 
    # print(list(successor_map.keys())[:10])  # Print the first 10 keys

    # limit print to first 10
    if (ngram == 2):
        print(successor_map['romeo'][:10])
    elif (ngram == 3):
        key = ('romeo', 'and')
        if key in successor_map:
            print( successor_map[key] )
            print( random.choice(successor_map[key]) )
        else:
            print("Key not found")

    # word0 = input("Enter a word: ")
    # word1 = random.choice(successor_map[word0])

    # print(word1)

    word1 = 'romeo'
    word2 = 'and'

    for i in range(50):
        print(word1, end=' ')
        successors = successor_map[(word1, word2)]
        word3 = random.choice(successors)

        word1 = word2
        word2 = word3

if __name__ == "__main__":
    main()