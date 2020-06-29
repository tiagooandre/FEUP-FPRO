def longest_prefix(words):
    def commonPrefix(left,right):
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]

    def find_longestCommonPrefix(words, left_index, right_index):
        if left_index == right_index:
            return words[left_index]
        # recursive call
        else:
            mid_index = (left_index + right_index)//2
            lcpLeft = find_longestCommonPrefix(words,left_index, mid_index)
            lcpRight = find_longestCommonPrefix(words,mid_index+1,right_index)
            return commonPrefix(lcpLeft,lcpRight)

    if not words: return ""
    return find_longestCommonPrefix(words, 0, len(words)-1)
print(longest_prefix(['apple', 'apply', 'ape', 'april']))