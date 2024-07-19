import json
import pprint
from collections import defaultdict

EXCLUDE_SHORT_WORDS = True

with open('data/words_as_tree.json', 'r') as f:
    words = json.load(f)


def find_valid_words_starting_with(cur_path, word):
    if "valid" in cur_path and gold_letter in word:
        if EXCLUDE_SHORT_WORDS and len(word) > 3:
            valid_words.append(word)
    for k in cur_path.keys():
        if k == "valid":
            continue
        if k in letters:
            find_valid_words_starting_with(cur_path=cur_path[k], word=word + k)


def run():
    for letter in letters:
        cur_path = words[letter]
        find_valid_words_starting_with(cur_path=cur_path, word=letter)

    print("Found {} valid words".format(len(valid_words)))
    nice_result = defaultdict(list)
    [nice_result[len(w)].append(w) for w in valid_words]
    for k, v in nice_result.items():
        print("{}: \n{}".format(k, pprint.pformat(v, indent=1, width=100, compact=True)))


if __name__ == "__main__":
    letters = [c for c in "wdlgine"]
    # The first letter is always the GOLD LETTER!!!
    gold_letter = letters[0]
    valid_words = []
    run()
