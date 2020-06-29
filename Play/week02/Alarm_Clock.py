h = int(input("H: "))
m = int(input("M: "))

h += 6
m += 51

while h > 24:
    h -= 24
    break

while m >= 60:
    m -= 60
    h += 1
    break

while h >= 24 and m >= 60:
    h -= 24
    m -= 60
    h += 1
    break

while h < 10:
    h = "0" + str(h)
    break

while m < 10:
    m = "0" + str(m)
    break

print("%s:%s" %(h, m))