#Given 2 integer arrays, return their intersection

def intersection(a, b):
    alen = len(a)
    blen = len(b)
    ans = []

#to cach which array is smaller. Not necessary if it's stated that a or b is the bigger array.
    if alen > blen:
        smaller = b
        bigger = a
    elif blen > alen:
        smaller = a
        bigger = b
    elif alen == blen:
        smaller = a
        bigger = b

    length = min(alen, blen)

    for i in range(length):
        if (smaller[i] in bigger) and (smaller[i] not in ans):
            ans.append(smaller[i])
    print (ans)

# a = [2, 4, 4, 2]
# b = [2, 4]

# a = [1, 2, 3, 3,]
# b = [3, 3]
#
# a = [2, 4, 6, 8]
# b = [1, 3, 5, 7]
#
# intersection(a, b)