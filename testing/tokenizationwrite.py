from collections import Counter

# import spacy
# nlp = spacy.load("en_core_web_sm")


def main():
    filename = 'data/romeoandjuliet.txt'
    reader = open(filename)
    lines = reader.readlines()
    reader.close()

    # doc = nlp(' '.join(lines))
    
    punctuation = '.;,-“’”:?—‘!()_[]='

    tokenized_text = []

    for line in lines:
        words = line.split()
        for word in words:
            cleaned_word = word.strip(punctuation).lower()
            tokenized_text.append(cleaned_word)

    print("TOKENIZED_TEXT: ", tokenized_text)

    # write the tokenized_text to a file
    with open('data/tokenized_text.txt', 'w') as writer:
        for word in tokenized_text:
            writer.write(word + '\n')
            


if __name__ == "__main__":
    main()