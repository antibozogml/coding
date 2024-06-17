List = list(map(int, input().split()))
a = int(input())
b = int(input())
# x = List[b]
# b = List[a]
# a = x
# List[a] = [b]
# List[x] = [a]
tmp = List[a]
List[a] = List[b]
List[b] = tmp
print (List)