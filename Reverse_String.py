##Take in a string and output the reverse
def reverse(s):
    reversestr = ""
    for i in s[::-1]:
        reversestr += i
    print (reversestr)

##Test Code
# s = "I am a Big Cat"
# reverse(s)