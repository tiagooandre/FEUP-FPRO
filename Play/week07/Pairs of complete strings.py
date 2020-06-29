def complete_pairs(s1, s2):
    alph = set("abcdefghijklmnopqrstuvwxyz")
    lista_new_words = []
    complete_words = []
    for word1 in s1:
        for word2 in s2:
            new_word = word1 + word2
            lista_new_words.append(new_word)

    for words in lista_new_words:
        if set(words) >= alph:
            complete_words.append(words)

    return set(complete_words)