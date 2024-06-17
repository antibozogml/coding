x = int(input())
lower = 0
upper = x + 1
while upper > 1 + lower:
    middle = (upper + lower) // 2
    if x >= middle**2:
        lower = middle
    else:
        upper = middle
print(lower)