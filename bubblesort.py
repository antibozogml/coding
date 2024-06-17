List = (list(map(int, input().split())))
i = 0
j = 0
z = 0
while j != len(List)-1:
    j = 0
    i = 0
    while i < len(List) - 1:
        if List[i] > List[i+1]:
            List[i],List[i+1] = List[i+1],List[i]
            j = 0
        else:
            j += 1
        z += 1
        i += 1
print(z)