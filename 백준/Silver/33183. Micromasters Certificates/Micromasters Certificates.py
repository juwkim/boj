from itertools import combinations

l = [*map(str.rstrip, open(0))]
micromasters = []
for i in range(1, len(l) - 1):
    for j in range(1, len(l[i]) - 1):
        if l[i][j] != "+" or l[i-1][j] == '|' or l[i][j-1] == '-':
            continue
        x, y = i + 1, j + 1
        while l[i][y] == '-': y += 1
        cur = set()
        while l[x][j] == '|':
            s = l[x][j+1:y].lower().replace(" ", "")
            if s: cur.add(s)
            x += 1
        micromasters.append(cur)
print(min(len(a | b | c) for a, b, c in combinations(micromasters, 3)))