import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
names = {input(): [] for _ in range(n)}
for _ in range(int(input())):
    a, b = input().split()
    names[a].append(b)
    names[b].append(a)
    
visited = set()
ans = 0
for name in names:
    if name in visited:
        continue
    ans += 1
    stack = [name]
    visited.add(name)
    while stack:
        current = stack.pop()
        for friend in names[current]:
            if friend in visited:
                continue
            visited.add(friend)
            stack.append(friend)
print(ans)