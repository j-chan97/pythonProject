# Given a string, return whether or not it uses capitalisation correctly
# A string correctly uses capitalisation is all letters are capitalised,
# no letters are capitalised or only the first letter is capitalised

def correct_capita(s):
    slen = len(s)
    ctr = 0
    for i in s:
        if "A" <= i <= "Z":
            ctr +=1
    if ctr == slen or ctr == 0:
        print (True)
    elif ctr == 1 and "A" <= s[0] <= "Z":
        print(True)
    else:
        print (False)

#Testing
# s = "compTer"
#
# correct_capita(s)