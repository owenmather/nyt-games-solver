import json
import pprint
from collections import defaultdict

EXCLUDE_SHORT_WORDS = True

with open('data/words_as_tree.json', 'r') as f:
    words = json.load(f)


def find_valid_words_starting_with(cur_path, word, idx):
    if "valid" in cur_path:
        if EXCLUDE_SHORT_WORDS and len(word) > 3:
            valid_words.append(word)
    for k in cur_path.keys():
        if k == "valid":
            continue
        if k in valid_words[idx]:
            try:
                find_valid_words_starting_with(cur_path=cur_path[k], word=word + k, idx=get_line[k])
            except Exception as e:
                x = 1


# noinspection DuplicatedCode
def run():
    for idx, line in enumerate(letters):
        for c in "".join(line):
            cur_path = words[c]
            find_valid_words_starting_with(cur_path=cur_path, word=c, idx=idx)

    # print("Found {} valid words".format(len(valid_words)))
    # nice_result = defaultdict(list)
    # [nice_result[len(w)].append(w) for w in valid_words]
    # for k, v in nice_result.items():
    #     print("{}: \n{}".format(k, pprint.pformat(sorted(v), indent=1, width=100, compact=True)))
    pprint.pprint(sorted(valid_words, key=lambda x: len(set(x))))


if __name__ == "__main__":
    letters = [["h", "l", "p"], ["k", "a", "t"], ["c", "n", "i"], ["y", "e", "o"], ]
    optimal_paths = []
    valid_words = []
    get_line = {}
    for i in range(len(letters)):
        for c in letters[i]:
            get_line[c] = i
        remaining_letters = letters.copy()
        remaining_letters.pop(i)
        valid_letters = remaining_letters
        valid_words.append("".join(["".join(x) for x in valid_letters]))
    run()
