Array = (list(map(int, input().split())))
x = int(input())
def BinarySearch(Array, x):
    lower = -1
    upper = len(Array)
    while lower + 1 < upper:
        middle = (upper + lower) // 2
        if x < Array[middle]:
            upper = middle
        else:
            lower = middle
    return upper
print(BinarySearch(Array, x))