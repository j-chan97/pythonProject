## Take in an input string s and determine if it's a palindrome, excluding all non alphanumerical indexes
def is_palindrome(s):
    s = s.lower()
    slen = len(s)
    left_pointer = 0
    right_pointer = slen - 1
    while left_pointer < right_pointer:
        if s[left_pointer].isalnum() != True:
            left_pointer += 1
        elif s[right_pointer].isalnum() != True:
            right_pointer -= 1
        elif s[left_pointer] == s[right_pointer]:
            left_pointer += 1
            right_pointer -= 1
        else:
            print (False)
            break
    print (True)

## test function
# s = "A man, a plan, a canal: Panama"
# is_palindrome(s)