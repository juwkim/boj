n = int(input())
a = input()
ans = 1
for _ in range(n - 1):
    ans = max(ans, min(len(a), len(b:=input())))
    a = b
print(ans)