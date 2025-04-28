"""
utils.py

Utility functions for text processing and n-gram generation
"""

import random
import ast
import json
import time
import os

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BLACK = '\033[30m'

LIGHT_RED = '\033[91m'
LIGHT_GREEN = '\033[92m'
LIGHT_BLUE = '\033[94m'
LIGHT_YELLOW = '\033[93m'
LIGHT_MAGENTA = '\033[95m'
LIGHT_CYAN = '\033[96m'

base_dir = os.path.dirname(__file__)
# go outside the scripts directory
base_dir = os.path.abspath(os.path.join(base_dir, '..'))  # go to the parent directory

def tokenize(filename, ngram=2, successor_map=None) -> dict:
    reader = open(filename)
    lines = reader.readlines()
    reader.close()
    
    punctuation = '.;,-“’”:?—‘!()_[]='

    if successor_map is None:
        successor_map = {}
    
    window = []

    for line in lines:
        for word in line.split():
            cleaned_word = word.strip(punctuation).lower()
            window.append(cleaned_word)

            successor_map = update_successor_map(window, successor_map, ngram)

    return successor_map

def update_successor_map(window, successor_map, ngram) -> dict:
    if ngram == 2:
        if len(window) == 2:
            if window[0] not in successor_map: # first instance of key and value
                successor_map[window[0]] = [(window[1], 1)]
            else:
                # second instance of key and value
                for i, (word, freq) in enumerate(successor_map[window[0]]):
                    if word == window[1]:
                        successor_map[window[0]][i] = (word, freq + 1)
                        break
                else: # second instance of key but new value
                    successor_map[window[0]].append((window[1], 1))
            window.pop(0)
    else:
        if len(window) == ngram:
            key = tuple(window[:-1])
            value = window[-1]
            if key not in successor_map: # first instance of key and value
                successor_map[key] = [(value, 1)]
            else:
                # second instance of key and value
                for i, (word, freq) in enumerate(successor_map[key]):
                    if word == value:
                        successor_map[key][i] = (word, freq + 1)
                        break
                else: # second instance of key but new value
                    successor_map[key].append((value, 1))
            window.pop(0)
    return successor_map

def write_successor_map(successor_map, ngram, action='w', extension='json'):
    filepath = ""
    if ngram == 2:
        # filepath=f'data/grams/_bigram/shakespeare_bigram.{extension}'
        filepath=os.path.join(base_dir, 'data', 'grams', '_bigram', f'shakespeare_bigram.{extension}')
    else:
        # filepath=f'data/grams/{ngram}gram/shakespeare_{ngram}gram.{extension}'
        filepath=os.path.join(base_dir, 'data', 'grams', f'{ngram}gram', f'shakespeare_{ngram}gram.{extension}')

    serializable_map = {str(key): value for key, value in successor_map.items()} 

    
    with open(filepath, 'w') as writer:
        json.dump(serializable_map, writer)

def load_successor_map(ngram, debug=True):
    tick = time.time()
    filepath = ""
    if ngram == 2:
        # filepath = 'data/grams/_bigram/shakespeare_bigram.json'
        filepath = os.path.join(base_dir, 'data', 'grams', '_bigram', 'shakespeare_bigram.json')
    else:
        # filepath = f'data/grams/{ngram}gram/shakespeare_{ngram}gram.json'
        filepath = os.path.join(base_dir, 'data', 'grams', f'{ngram}gram', f'shakespeare_{ngram}gram.json')
    
    with open(filepath, 'r') as reader:
        serializable_map = json.load(reader) 
    
    # convert string keys back to tuples
    if ngram == 2:
        successor_map = serializable_map
    else:
        successor_map = {ast.literal_eval(key): value for key, value in serializable_map.items()}
    tock = time.time() - tick
    if debug:
        print(f"\tLoaded successor map from file in: {tock:.2f}s")
        print("\t\tSuccessor map size: ", len(successor_map))
    else:
        print(f"{tock:.2f}") # DEBUG
    return successor_map

def load_test_quotes():
    filepath = os.path.join(base_dir, 'data', 'testing', 'quotes.json')  # adjust path from utils.py
    with open(filepath, 'r') as reader:
        quotes = json.load(reader)
    return quotes


def weighted_random_choice(successors):
    words, weights = zip(*successors)
    return random.choices(words, weights=weights, k=1)[0]


def print_examples(successor_map, ngram):

    # romeo and juliet
    seed_words1 = ['romeo', 'and', 'juliet', 'by', 'william', 'shakespeare']
    seed_words2 = ['thus', 'with', 'a', 'kiss', 'i', 'die']
    seed_words3 = ['o', 'romeo', 'romeo', 'wherefore', 'art', 'thou']
    seed_words4 = ['a', 'pair', 'of', 'star-crossed', 'lovers', 'take']
    seed_words5 = ['in', 'fair', 'verona', 'where', 'we', 'lay']

    # hamlet
    seed_words6 = ['to', 'be', 'or', 'not', 'to', 'be']


    # macbeth
    seed_words7 = ['fair', 'is', 'foul', 'and', 'foul', 'is', 'fair']
    seed_words8 = ["what's", 'done', 'cannot', 'be', 'undone', '--to' ]

    # king lear
    seed_words9 = ['when', 'we', 'are', 'born', 'we', 'cry']

    # henry iv part 1
    seed_words10 = ['the', 'king', 'hath', 'many', 'marching', 'in']

    # twelfth night
    seed_words11 = ['if', 'music', 'be', 'the', 'food', 'of', 'love']

    # a midsummer night's dream
    seed_words12 = ['love', 'looks', 'not', 'with', 'the', 'eyes']

    # much ado about nothing
    seed_words13 = ['some', 'cupid', 'kills', 'with', 'arrows', 'some']

    # othello
    seed_words14 = ['men', 'in', 'rage', 'strike', 'those', 'that']

    # the tempest
    seed_words15 = ["'hell", 'is', 'empty', 'and', 'all', 'the']

    # --

    # richard II (corpus 19)
    seed_words16 = ['brought', 'hither', 'henry', 'hereford', 'thy', 'bold']

    # henry V (corpus 20)
    seed_words17 = ['o', 'for', 'a', 'muse', 'of', 'fire']

    
    words = seed_words17[:ngram-1]

    print("WORDS: ", words)

    if ngram == 2:
        if words[0] in successor_map:
            print(f"SUCCESSOR MAP 10/{len(successor_map[words[0]])}: ", successor_map[words[0]][:10], "...")
            # print("WEIGHTED CHOICE: ", weighted_random_choice(successor_map[words[0]]))
    elif ngram >= 3:
        key = tuple(words)
        if key in successor_map:
            print("SUCCESSOR MAP: ", successor_map[key])
            # print("WEIGHTED CHOICE: ", weighted_random_choice(successor_map[key]))
        else:
            print("Key not found")

    print("----------------")
    for i in range(50): 
        if ngram == 2:
            if i < ngram - 1:
                print(f"{RED}{words[0]}{RESET}", end=' ')
            else:
                print(words[0], end=' ')
            next_word = weighted_random_choice(successor_map[words[0]])
            words[0] = next_word
        elif ngram >= 3:
            if i < ngram - 1:
                print(f"{RED}{words[0]}{RESET}", end=' ')
            else:
                print(words[0], end=' ')
            key = tuple(words)
            if key in successor_map:
                next_word = weighted_random_choice(successor_map[key])
                words.pop(0)
                words.append(next_word)
            else:
                print("Key not found")
                break
    print("\n----------------")

def query_inference(successor_map, ngram, num_prediction_words, context) -> str:
    if len(context) < ngram - 1:
        return "ERROR: context is too short for the {ngram}-gram model"
    context = context.split()  # list of words
    result = " ".join(context) + " "  # start the result with the initial context

    # check if context EXISTS in successor_map
    if ngram == 2:
        if context[0] not in successor_map:
            return "ERROR: context is not in successor_map"
    elif ngram >= 3:
        key = tuple(context[:ngram - 1])
        if key not in successor_map:
            return "ERROR: context is not in successor_map"

    for i in range(num_prediction_words): # 50 prediction words

        if ngram == 2:
            if context[0] in successor_map:
                next_word = weighted_random_choice(successor_map[context[0]])
                result += f"{next_word} "
                context[0] = next_word
            else:
                break
        elif ngram >= 3:
            key = tuple(context[-(ngram - 1):])  # use the last (ngram - 1) words as the context
            if key in successor_map:
                next_word = weighted_random_choice(successor_map[key])
                result += f"{next_word} "
                context.append(next_word)  
                context.pop(0)  
            else:
                break

    return result


def top_k_successors(successor_map, context, k=5):

    if len(context) < 1:
        raise ValueError("Context must be at least 1 word long")
    
    if len(context) == 1:
        context = context[0]
    elif len(context) > 1:
        context = tuple(context)
    
    if context not in successor_map:
        return []
    
    successors = successor_map[context]
    successors.sort(key=lambda x: x[1], reverse=True) 
    return successors[:k] 

def update_metrics(guesses, target, TP, FP, FN):
    guess_words = [guess[0] for guess in guesses]

    if target in guess_words:
        TP += 1
        # print(f"Target: {target}, Guesses: {guess_words}", f"{GREEN}Target found{RESET}") # DEBUG 
    else:
        FN += 1
        # print(f"Target: {target}, Guesses: {guess_words}", f"{RED}Target not found{RESET}") # DEBUG

    for guess in guesses:
        if guess != target:
            FP += 1

    return TP, FP, FN

def choose_color(ngram):
    colors = [(LIGHT_RED, 2), (LIGHT_GREEN, 3), (LIGHT_BLUE, 4), (LIGHT_YELLOW, 5), (LIGHT_MAGENTA, 6), (LIGHT_CYAN, 7)]
    for color, n in colors:
        if ngram == n:
            return color
    return LIGHT_RED

def evaluate_metrics(TP, FP, FN, ngram):

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = TP / (TP + FP + FN) if (TP + FP + FN) > 0 else 0

    title_color = choose_color(ngram)
    if ngram == 2:
        ngram = "bigram"
    else:
        ngram = f"{ngram}gram"

    print(f"\n{title_color}Evaluation Metrics for {ngram}:{RESET}")
    print(f"{BLACK}TP: {TP}, FP: {FP}, FN: {FN}{RESET}")
    print(f"{BLUE}Precision:{RESET} {precision:.4f}, {YELLOW}Recall:{RESET} {recall:.4f}, {GREEN}F1:{RESET} {f1:.4f}, {RED}Accuracy:{RESET} {accuracy:.4f}\n")
    return precision, recall, f1, accuracy