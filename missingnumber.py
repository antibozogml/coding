n = int(input())
MissingNumber = (list(map(int, input().split())))
FrequencyList = [0] * (n)
i = 0
while i < n-1:
    FrequencyList[MissingNumber[i]-1] = 1
    i += 1
i = 0
while i < n-1:
    if 0 == FrequencyList[i]:
        break
    i += 1
print (i+1)