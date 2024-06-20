#given two strings, s and t, check if they are anagrams of each other

def is_anagram(s, t):
    print(sorted(s) == sorted(t))

#test

# s = "cat"
# t = "tac"

# s = "listen"
# t = "silent"

# s = "program"
# t = "function"

# is_anagram(s, t)