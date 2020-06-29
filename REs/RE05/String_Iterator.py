def rm_letter_rev(ch, astr):
    astr = astr[::-1]
    astr = astr.replace(ch, "")

    return astr

print(rm_letter_rev('s', 'A style guide is about consistency'))