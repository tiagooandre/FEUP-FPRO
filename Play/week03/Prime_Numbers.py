lower = int(input("Lower: "))
upper = int(input("Upper: "))

print("Prime numbers between", lower, "and", upper, "are:", end = " ")

for i in range(lower, upper+1, 1):
   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           print(i, end = " ")

