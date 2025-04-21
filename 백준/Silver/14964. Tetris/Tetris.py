def normalize(shape):
    xs, ys = zip(*shape)
    mx, my = min(xs), min(ys)
    return tuple(sorted((x - mx, y - my) for x, y in shape))

shapes = []
for shape in ((0, 0), (0, 1), (1, 0), (1, 1)), ((0, 0), (1, 0), (2, 0), (3, 0)), ((0, 1), (0, 2), (1, 0), (1, 1)), ((0, 1), (1, 1), (1, 0), (2, 0)), ((0, 1), (1, 0), (1, 1), (1, 2)):
    variants = set()
    for _ in range(4):
        variants.add(normalize(shape))
        shape = [(y, -x) for x, y in shape]
    shapes.append(variants)

N, M = map(int, input().split())
grid = [input() for _ in range(N)]
visited = [bytearray(M) for _ in range(N)]
count = [0] * 5
for i in range(N):
    for j in range(M):
        if grid[i][j] == '.' or visited[i][j]:
            continue
        color = grid[i][j]
        st = [(i, j)]
        comp = [(i, j)]
        visited[i][j] = True
        while st:
            x, y = st.pop()
            for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == color:
                    visited[nx][ny] = True
                    comp.append((nx, ny))
                    st.append((nx, ny))
        shape = normalize(comp)
        for a in range(5):
            if shape in shapes[a]:
                count[a] += 1
                break
print(*count, sep='\n')