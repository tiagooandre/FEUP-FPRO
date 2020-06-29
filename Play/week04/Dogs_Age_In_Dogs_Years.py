def dogs(h_age):
    if (h_age <= 2):
        h_age = h_age * 10.5
        return h_age
    else:
        h_age = (2*10.5) + ((h_age - 2)*4)
        return h_age

print(dogs(4))