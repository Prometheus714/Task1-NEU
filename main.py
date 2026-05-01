def is_pali(word):
    word = word.lower()
    return word == word[::-1]