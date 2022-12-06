N, M = map(int, input().split())
check = [False for _ in range(M)]
temp = 0
for _ in range(N):
    state = input()
    flag = 0
    for i in range(M):
        if state[i] == 'X':
            flag = 1
            check[i] = True
    temp += flag
print(max(N - temp, M - sum(check)))