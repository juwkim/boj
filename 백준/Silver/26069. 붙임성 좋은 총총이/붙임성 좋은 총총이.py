ans = {"ChongChong"}
for _ in range(int(input())):
    a, b = input().split()
    if a in ans:
        ans.add(b)
    elif b in ans:
        ans.add(a)
print(len(ans))