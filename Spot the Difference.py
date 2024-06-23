## Given 2 strings, s and t, which only consist of lower case characters, t is generated
##by shuffing the letters in s as well as potentially adding an additional random character
##Return the letter that was randomly added to t if it exists, otherwise, return " ".
##assume at most one additional character can be added to t

# s = "foobar"
# t = "barfoot"

# s = "ide"
# t = "idea"

# s = "coding"
# t = "ingcod"
def spot_the_difference(s, t):

    if len(s) == len(t):
        return(" ")

    for char in t:
        if char not in s:
            return (char)

spot_the_difference(s, t)