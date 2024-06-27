#Given a string, return the index of its first unique character. If a unique character does not exist, return -1

def first_unique_character(s):
    slen = len(s)
    dictionary = {}

    for char in s:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1

    for i in range(slen):
        if dictionary[s[i]] == 1:
            return (i)

    return (-1)

# s = "abcabd"

# s = "thedailybyte"
#
# s = "developer"
#
# s = "aabbcc"

first_unique_character(s)