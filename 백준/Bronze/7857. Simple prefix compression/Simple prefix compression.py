N = int(input())
a = input()
ans = len(a)
for i in range(N-1):
    b = input()
    ans += len(b) + 1
    for s, t in zip(a, b):
        if s == t:
            ans -= 1
        else:
            break
    a = b
print(ans)