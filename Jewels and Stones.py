## given a string representing your stones and another string representing a list of jewels,
## return the numer of stones that you have that are alwaso jewels

# jewels = "abc"
# stones = "ac"

# jewels = "Af"
# stones = "AaaddfFf"

# jewels = "AYOPD"
# stones = "ayopd"

def is_jewel(jewels, stones):
    ctr = 0

    for char in jewels:
        if char in stones:
            ctr += 1
    print(ctr)

# is_jewel(jewels, stones)