def bubble_sort(alist):
    flag = False
    for i in range(len(alist)-1):
        if alist[i] > alist[i+1]:
            aux = alist[i]
            alist[i] = alist[i+1]
            alist[i+1] = aux
            flag = True
    if flag == False:
        return alist
    else:
        return bubble_sort(alist)

print(bubble_sort([192, 12378, 12, -113, 12.5, 10]))