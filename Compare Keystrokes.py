#Given 2 strings s and t, which represents a sequence of keystrokes, where # denotes a backspace,
# return whether or not the sequences produce the same results

def compare_keystrokes(s, t):
    slen = len(s)
    tlen = len(t)
    new_s = ""
    new_t = ""

    for schar in s:
        if schar != "#":
            new_s += schar
        else:
            new_s = new_s[:-1]
    for tchar in t:
        if tchar != "#":
            new_t += tchar
        else:
            new_t = new_t[:-1]

    print (bool (new_s == new_t))






# s = "ABC#"
# t = "CD##AB"
#
# s = "como#pur#ter"
# t = "computer"

s = "cof#dim#ng"
t = "code"

compare_keystrokes(s, t)