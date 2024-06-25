#Given 2 strings representing sentences, return the words that are not common to both strings.

# s = "the quick"
# t = "brown fox"

# s = "the tortoise beat the hare"
# t = "the tortoise lost to the hare"

def uncommonwords(s, t):
    s = s.split()
    t = t.split()
    slen = len(s)
    tlen = len(t)
    ans = []
    for i in range(slen):
        if s[i] not in t:
            ans.append(s[i])

    for i in range (tlen):
        if t[i] not in s:
            ans.append(t[i])

    return (ans)

# uncommonwords(s, t)

