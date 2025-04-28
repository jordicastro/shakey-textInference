
from collections import Counter

import sys
from utils import tokenize, write_successor_map, load_successor_map, print_examples

def main():
    ngram = 2
    successor_map = {} # successor_map = None

    if len(sys.argv) > 1:
        ngram = int(sys.argv[1])

    # load existing successor map and test it
    successor_map = load_successor_map(ngram, debug=True)
    print_examples(successor_map, ngram)

if __name__ == "__main__":
    main()