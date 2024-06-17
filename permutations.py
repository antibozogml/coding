x = int(input())
Arr = []
for i in range(x):
    Arr.insert(0, i + 1)
def Permute(Arr, x):
    if x == len(Arr):
        print(Arr)
        return
    for i in range(x, len(Arr)):
        a = Arr[x]
        Arr[x] = Arr[i]
        Arr[i] = a
        Permute(Arr, x+1)
        a = Arr[x]
        Arr[x] = Arr[i]
        Arr[i] = a
Permute(Arr, 0)