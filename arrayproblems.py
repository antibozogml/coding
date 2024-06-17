#sum,minimum,maximum
AnArray = (list(map(int, input().split())))
def max(AnArray):
    i = 0
    x = AnArray[1]
    while i < len(AnArray):
        if x < AnArray[i+1]:
            x = AnArray[i+1]
        i += 1