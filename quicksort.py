arr = (list(map(int, input().split())))
lower = 0
upper = len(arr)

def Quicksort(lower, upper):
    if upper - lower <= 1:
        return
    print(upper - 1)
    print(lower)
    k = Partition(lower, upper)
    print(k)
    print(arr)
    Quicksort(lower, k)
    Quicksort(k + 1, upper)

def Partition(lower, upper):
    global arr
    x = upper - 1
    k = arr[x]
    j = lower
    for i in range(lower, x):
        if arr[i] < k:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[x], arr[j] = arr[j], arr[x]
    return j
Quicksort(lower, upper)
# Partition(lower, upper)
print(arr)