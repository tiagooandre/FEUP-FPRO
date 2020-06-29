def last_man_standing(alist, step):
    if(len(alist)==1):
        return alist[0]

    curr = (0+step-1)%len(alist)
    alist.remove(alist[curr])
    if(curr > len(alist)):
        curr = 0
    alist = alist[curr:] + alist[:curr]
    return last_man_standing(alist, step)