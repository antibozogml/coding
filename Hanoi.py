# base case when right = x where x is left in the beginning
# yay
N = int(input())
moves = []
def moveto(x, cur, target): #left is 0, middle is 1, right is 2
    if x == 0: return
    moveto(x-1, cur, 3 - cur - target)
    moves.append([cur+1, target+1])
    moveto(x-1, 3 - cur - target, target)

moveto(N, 0, 2)
print(len(moves))
for move in moves:
    print(*move)