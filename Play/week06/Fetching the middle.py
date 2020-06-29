def fetch_middle(llists):
    new_list = []
    for i in llists:
        if (len(i) % 2 == 0):
            pos = int(len(i)/2)
            media = (i[pos] + i[pos-1])/2
            new_list.append(media)
        else:
            pos = i[int(len(i)/2)]
            new_list.append(pos)

    return new_list

print(fetch_middle([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]))