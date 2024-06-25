

def longestCommonPrefix(strs):
    strs = sorted(strs)
    ans = ""
    first = strs[0]
    last = strs[-1]
    flen = len(first)
    llen = len(last)
    length = min(flen, llen)
    for i in range(length):
        if first[i] != last[i]:
            return ans
        else:
            ans += first[i]

    return ans

# strs = ["flower","flow","flight"]
#
# strs = ["dog","racecar","car"]
#
# longestCommonPrefix(strs)