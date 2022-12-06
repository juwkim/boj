names = [input().split() for _ in range(int(input()))]
names.sort(key=lambda x: (x[1], x[0])) 
for name in names:
    print(*name)