#Given a string s remove all the vowels it contains and return the resulting string.
#Note: In this problem y is not considered a vowel.

def removeVowel(string):
    vowel_dict = {'a','e','i','o','u'}
    new_string = ""

    for char in string:
        if char not in vowel_dict:
            new_string = new_string + char
    print (new_string)

# s = "aeiou"
# s = "byte"
s = "xyz"

removeVowel(s)