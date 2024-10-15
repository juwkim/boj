import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
A = [[*input()] for _ in range(R)]
ans = 0
for i in range(R - 1, -1, -1):
    st = [(i, 0)]
    while st:
        x, y = st.pop()
        A[x][y] = 'x'
        if y == C - 1:
            ans += 1
            break
        ny = y + 1
        for nx in range(x - 1, x + 2):
            if 0 <= nx < R and A[nx][ny] == '.':
                st.append((nx, ny))    
print(ans)