def is_orthogonal(mx):
    mxt = [[mx[j][i] for j in range(len(mx))] for i in range(len(mx[0]))]

    product = []
    for i in range(len(mx)): #row
        this_row = []
        for j in range(len(mx[i])): #line
            this_elem = 0
            for k in range(len(mx[0])):
                this_elem += mx[j][k] * mxt[k][i]
            this_row.append(this_elem)
        product.append(this_row)

    identity = [[1 if j == i else 0 for i in range(len(mx))] for j in range(len(mx))]

    return product == identity

print(is_orthogonal([[-1, 0], [0, 1]]))