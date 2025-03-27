from collections import Counter


def main():
    filename = 'data/romeoandjuliet.txt'
    reader = open(filename)
    lines = reader.readlines()
    reader.close()
    
    punctuation = '.;,-“’”:?—‘!()_[]='

    freq_dict = {}

    for line in lines:
        words = line.split()
        for word in words:
            cleaned_word = word.strip(punctuation).lower()
            if cleaned_word in freq_dict:
                freq_dict[cleaned_word] += 1
            else:
                freq_dict[cleaned_word] = 1

    # print("FREQ_DICT: ", freq_dict)
    # print("LENGTH: ", len(freq_dict))

    # ordering by frequency
    sorted_freq_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
    print("SORTED_FREQ_DICT: ", sorted_freq_dict)

if __name__ == "__main__":
    main()