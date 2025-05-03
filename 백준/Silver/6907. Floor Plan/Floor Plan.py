import sys
input = sys.stdin.readline

flooring, r, c = map(int, [input() for _ in range(3)])
grid = [[*input()] for _ in range(r)]
room_sizes = []
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'I':
            continue
        size = 1
        grid[i][j] = 'I'
        st = [(i, j)]
        while st:
            x, y = st.pop()
            for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '.':
                    grid[nx][ny] = 'I'
                    size += 1
                    st.append((nx, ny))
        room_sizes.append(size)
cnt = 0
for size in sorted(room_sizes, reverse=True):
    if flooring < size:
        break
    flooring -= size
    cnt += 1
print(f"{cnt} room{'' if cnt == 1 else 's'}, {flooring} square metre(s) left over")