import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.utils import load_successor_map, query_inference

def main() -> str:

    successor_map = load_successor_map(ngram=4, debug=False)
    print()
    print(f"Successor Map of 'if music be': {successor_map[tuple('if music be'.split())]}")
    print(f"Successor Map of 'music be the': {successor_map[tuple('music be the'.split())]}")
    print(f"Successor Map of 'be the food': {successor_map[tuple('be the food'.split())]}")
    print(f"Successor Map of 'the food of': {successor_map[tuple('the food of'.split())]}")
    print()

        
if __name__ == "__main__":
    main()