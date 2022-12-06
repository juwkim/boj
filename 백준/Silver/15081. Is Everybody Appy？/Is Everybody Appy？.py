buf = []
Set = set()
for _ in range(int(input())):
    n, *l = input().split()
    for app in l:
        if app not in Set:
            buf.append(app)
            Set.add(app)
            break
print(*buf)