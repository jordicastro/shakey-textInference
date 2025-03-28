
from collections import Counter
import random

import sys
from utils import tokenize, write_successor_map, load_successor_map, print_examples

def main():
    ngram = 2
    filename = 'data/corpora/romeoandjuliet.txt'
    successor_map = {} # successor_map = None

    if len(sys.argv) > 1:
        ngram = int(sys.argv[1])
        if len(sys.argv) > 2:
            filename = sys.argv[2]

    # ADD new key-terms from new corpus to existing successor map
    # 1. load existing successor map
    successor_map = load_successor_map(ngram)
    # 2. tokenize new corpus using existing successor map
    successor_map = tokenize(filename=filename, ngram=ngram, successor_map=successor_map)
    # 3. write new successor map to file
    write_successor_map(successor_map, ngram, 'w', 'json')
    # 4. print examples from both corpora
    # print_examples(successor_map, ngram)

if __name__ == "__main__":
    main()