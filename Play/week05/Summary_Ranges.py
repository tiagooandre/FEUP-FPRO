def summary_ranges(astring):

    astring = [int(i) for i in astring.split(",")]
    length = len(astring)

    if length == 0:
        return []
    if length == 1:
        return [str(astring[0])]

    res = []
    low_b = astring[0]
    num_steps = 1

    for i in range(1, length):
        if astring[i] > low_b +  num_steps:
            output = str(low_b)
            if num_steps > 1:
                output += "->" + str(astring[i-1])
            res.append(output)
            low_b = astring[i]
            num_steps = 0

        if i == length-1:
            output = str(low_b)
            if low_b != astring[i]:
                output += "->" + str(astring[i])
            res.append(output)
        num_steps += 1

    return ",".join(res)

print(summary_ranges('0,1,2,3,4,5,7,10,11,20,21'))