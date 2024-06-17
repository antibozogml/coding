List = (list(map(int, input().split())))
def Sum(List):
    i = 0
    x = 0
    while i < len(List):
        x += List[i]
        i += 1
    return x
print('The sum of all the numbers within the list is ' + str(Sum(List)) + '.')