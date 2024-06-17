List = (list(map(int, input().split())))

def Index(List, n):
    i = 0
    while i < len(List):
        if n == List[i]:
            return i
        i += 1
    return i

def Minimum(List):
    x = List[0]
    i = 1
    while i < len(List):
        x = min(List[i], x)
        i += 1
    return x

def SortListSmallLarge(List):
    N = len(List)
    for i in range(N):
        List2 = List.copy()
        for _ in range(i):
            List2.pop(0)
        y = Index(List2, Minimum(List2)) + i
        List[i], List[y] = List[y], List[i]
        print(List)
    return List
print(SortListSmallLarge(List))