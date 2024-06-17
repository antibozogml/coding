# preconditions: Array is sorted. x is the element for which we want to find the index of. 
# return an index where x is at, or return -1 if there is none.
Array = (list(map(int, input().split())))
x = int(input())
def BinarySearch(Array, x, lower, upper): 
    middle = (upper + lower) // 2
    if x == Array[middle]:
        return middle
    if upper - lower == 1:
        return -1
    elif x > Array[middle]:
        return BinarySearch(Array, x, middle, upper)
    else:
        return BinarySearch(Array, x, lower, middle)
print(BinarySearch(Array, x, 0, len(Array)))