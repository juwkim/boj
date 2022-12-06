def check():
    return abs(X - a) <= 1 and abs(Y - b) <= 1

X, Y = map(int, input().split())
K = int(input())
a, b = 0, 0
temp = []
if check():
    temp.append(0)

move = input()
for i in range(K):
    a += (move[i] == 'I') - (move[i] == 'Z')
    b += (move[i] == 'S') - (move[i] == 'J')
    
    if check():
        temp.append(i+1)
if temp:
    print(*temp)
else:
    print(-1)