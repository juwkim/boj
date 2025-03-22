import sys
input = sys.stdin.readline

R, C = map(int, input().split())
a = [[*input()] for _ in range(R)]
x, y = -1, -1
for i in range(R):
    for j in range(C):
        if a[i][j] == 'S':
            x, y = i, j
            break
    if x != -1:
        break
ans = 1
st = [(x, y)]
while st:
    x, y = st.pop()
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and a[nx][ny] == '#':
            ans += 1
            a[nx][ny] = '.'
            st.append((nx, ny))
print(ans)