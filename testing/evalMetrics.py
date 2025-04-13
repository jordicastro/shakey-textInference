import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import load_successor_map, load_test_quotes, top_k_successors, update_metrics, evaluate_metrics


def main():
    if len(sys.argv) < 2:
        print("Usage: python evalMetrics.py <ngram>")
        return
    ngram = int(sys.argv[1])

    TP = 0
    FP = 0
    FN = 0

    quotes = load_test_quotes()
    print("Quotes loaded successfully: ", len(quotes))
    print("Quotes: ", quotes.keys())

    successor_map = load_successor_map(ngram, debug=False)

    for play, play_quotes in quotes.items():
        print(f"Play: {play}")
        for quote in play_quotes:
            tokens = quote.split()

            # quote is too small for ngram
            if len(tokens) < ngram:
                continue
            
            context = tokens[:ngram-1]
            target = tokens[ngram-1]
            
            guesses = top_k_successors(successor_map, context, k=5)
            print(f"guesses: {guesses}")

            TP, FP, FN = update_metrics(guesses, target, TP, FP, FN)

    print(f"TP: {TP}, FP: {FP}, FN: {FN}")
    precision, recall, f1, accuracy = evaluate_metrics(TP, FP, FN)
    
if __name__ == "__main__":
    main()