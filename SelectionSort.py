List = (list(map(int, input().split())))
n = int(input())

#Index code below

def Index(List, n):
    i = 0
    while i < len(List):
        if n == List[i]:
            return i
        i += 1
    return i
if Index(List, n) != -1:
    print ("The index is " + str(Index(List, n)) + '.')
else:
    print ('The index is -1. (Number is not in the list)')

#Largest Consecutive numbers difference code below

def ConsecutiveDifferences(List):
    y = 0
    i = 0
    while i < len(List)-1:
        x = abs(List[i] - List[i+1])
        y = max(x,y)
        i += 1
    return y

print ('The largest consecutive difference is ' + str(ConsecutiveDifferences(List)) + '.')

#Maximum of List code below

def Maximum(List):
    x = 0
    i = 1
    while i < len(List):
        if List[x] < List[i]:
            x = i
        i += 1
    return x

print ("The largest number's index is " + str(Maximum(List)) + '.')

#Minimum of List code below

def Minimum(List):
    x = List[0]
    i = 1
    while i < len(List):
        x = min(List[i], x)
        i += 1
    return x
print ('The smallest number is ' + str(Minimum(List)) + '.')

#Sum of numbers in the list code below

def Sum(List):
    i = 0
    x = 0
    while i < len(List):
        x += List[i]
        i += 1
    return x
print('The sum of all the numbers within the list is ' + str(Sum(List)) + '.')

#Sorted List from small to large code below

def SortListSmallLarge(List):
    z = 0
    List = List.copy()
    n = len(List)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if List[min_idx] > List[j]:
                min_idx = j
            z += 1
        List[i], List[min_idx] = List[min_idx], List[i]
    
    return z
print('The sorted list from small to large is ' + str(SortListSmallLarge(List)) + '.')