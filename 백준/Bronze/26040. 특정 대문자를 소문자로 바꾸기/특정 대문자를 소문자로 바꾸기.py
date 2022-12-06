A = input()
B = set(input().split())

ans = []
for i in A:
    if i.isupper() and i in B:
        ans.append(i.lower())
    else:
        ans.append(i)
print(*ans, sep='')