def reverse_word(word):
    reverse = ""
    for i in reversed(range(len(word))):
        reverse += word[i]
    return reverse