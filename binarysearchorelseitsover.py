Array = (list(map(int, input().split())))
x = int(input())
lower = 0
upper = len(Array)
while upper - lower > 0:
    middle = (upper + lower) // 2
    if Array[middle] == x:
        break
    if x >= Array[middle]:
        lower = middle
    else:
        upper = middle
print(middle)