N = int(input())
ans = set()
while N not in ans:
    ans.add(N)
    N = (N % 1000 // 10) ** 2
print(len(ans))