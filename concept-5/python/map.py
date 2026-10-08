words = [
    "apple",
    "banana",
    "apple",
    "cat",
    "dog",
    "tree",
    "banana",
    "elephant",
    "fox",
    "grape",
    "hat",
    "island",
    "jungle",
    "kite",
    "lemon",
    "mango",
    "apple",
    "orange",
    "pear",
    "queen",
]

def word_count(words: list = None):
    if not words:
        return {}
    word_count_table = {}
    for word in words:
        if word not in word_count_table:
            word_count_table[word] = 0
        word_count_table[word] += 1
    return word_count_table

print(word_count(words))