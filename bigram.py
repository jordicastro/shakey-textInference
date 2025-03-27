
from collections import Counter
import random


def main():
    filename = 'data/romeoandjuliet.txt'
    reader = open(filename)
    lines = reader.readlines()
    reader.close()
    
    punctuation = '.;,-“’”:?—‘!()_[]='

    successor_map = {}

    bigram1 = ('the', 'honour')
    bigram2 = ('honour', 'the')
    bigram3 = ('the', 'sanity')
    bigram4 = ('the', 'honour')
    bigrams = (bigram1, bigram2, bigram3, bigram4)

    for bigram in bigrams:
        if bigram[0] not in successor_map:
            successor_map[bigram[0]] = [bigram[1]]
        else:
            successor_map[bigram[0]].append(bigram[1])

    print(successor_map)
            

    print(successor_map['the'])

    word0 = input("Enter a word: ")
    word1 = random.choice(successor_map[word0])

    print(word1)

if __name__ == "__main__":
    main()