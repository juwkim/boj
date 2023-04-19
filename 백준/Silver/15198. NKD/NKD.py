k = int(input())
check = {}
for i in range(int(input())):
    check[input()] = i

print(*sorted(check, key=lambda x: -check[x])[:k])