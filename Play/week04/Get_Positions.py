def get_positions(sentence, word_list):

    sentence_split = sentence.split()
    output = []

    for i in range(len(sentence_split)):
        out = False
        for k in range(len(word_list)):
            if sentence_split[i] == word_list[k]:
                output.append(k)
                out = True
                word_list[k] = ""
                break
        if out == False:
            return("")
    output_ = (str(output[0]) + " " + str(output[1]))

    if output == " ":
        return (" ")
    else:
        return (output_)

print(get_positions('lousy world', ['hello', 'world', 'lousy']))