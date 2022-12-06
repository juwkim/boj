N, M = map(int, input().split())
left, right = 1, M

dist = 0
for _ in range(int(input())):
    apple = int(input())
    
    move = 0
    if apple < left:
        move = apple - left
    
    elif apple > right:
        move = apple - right
    
    left += move
    right += move
    dist += abs(move)

print(dist)