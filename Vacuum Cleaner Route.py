# given a string representing the sequence of moves a robot vacuum makes,
# return whether or not it will return to it's original position.

def VC_Route(route):
    rlen = len(route)
    x = 0
    y = 0
    for i in route:
        if i == "L":
            x -= 1
        elif i == "R":
            x += 1
        elif i == "U":
            y += 1
        elif i == "D":
            y -= 1
    if x == 0 and y == 0:
        return (True)
    else:
        return (False)

#To test
# r = "RUULLDRD"
#
# VC_Route(r)