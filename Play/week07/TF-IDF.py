from math import log

def tfidf(documents):
    lista = []
    for i in documents:
        for word in i.split(" "):
            if word.lower() not in lista:
                lista.append(word.lower())
    dicionario = dict()
    for each_word in lista:
        tf_idf_vec = []
        counter = 0
        for frases in documents:
            a = frases.lower().split()
            if each_word in a:
                counter += 1
        IDF = log(len(documents)/counter)
        for words1 in documents:
            b = words1.lower().split()
            if each_word in b:
                tf_idf_vec.append(round(b.count(each_word)*IDF, 3))
            else:
                tf_idf_vec.append((0.0))
        dicionario[each_word] = tf_idf_vec
    return dicionario

print(tfidf(['a', 'a one']))