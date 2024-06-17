arr = (list(map(int, input().split())))

def MergeSort(arr, lower, upper):
    if upper - lower <= 1:
        return
    x = lower + (upper - lower)//2
    MergeSort(arr, lower, x)
    MergeSort(arr, x, upper)
    Merge(arr, lower, upper, x)

def Merge(arr, lower, upper, k):
    arr2 = list()
    i = lower
    j = k
    while i != k and j < upper:
        if arr[i] <= arr[j]:
            arr2.append(arr[i])
            i += 1
        else:
            arr2.append(arr[j])
            j += 1
    while j < upper:
        arr2.append(arr[j])
        j += 1
    while i < k:
        arr2.append(arr[i])
        i += 1
    for  _ in range(lower, upper):
        arr[_] = arr2[_ - lower]
x = len(arr)
MergeSort(arr, 0, x)
print(arr)