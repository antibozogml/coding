List = (list(map(int, input().split())))
N = len(List)
for i in range(N):
    x = List[i]
    j = 1
    while j <= i and List[i-j] > x:
        List[i-j+1] = List[i-j]
        j += 1
        print(List)
    if (j > i):
        List[i-j+1] = x
    else:
        List[i-j] = x
    print(List)
    print(i)
print(List)