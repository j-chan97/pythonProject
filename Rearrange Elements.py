#GGiven an array of numbers,
#move all zeroes in the array to the end while maintaining the relative order of the other numbers.

def rearrangeElements(arr):
    arr.sort(key = lambda i: i == 0)
    print (arr)

arr = [3, 0, 1, 5, 0, 0]

rearrangeElements(arr)