import datetime

now = datetime.datetime.now();

h = 8 + now.hour
m = 30 + now.minute

if m >= 60:
    m -= 60
    h += 1

if h > 24:
    h -= 24

if h >= 24 and m >= 60:
    h -= 24
    m -= 60
    h += 1

if h < 10:
    h = "0" + str(h)

if m < 10:
    m = "0" + str(m)

print("%s:%s" %(h, m))