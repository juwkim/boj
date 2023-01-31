N = int(input())
ans = 1
while N >= ans * ans:
    N -= ans * ans
    ans += 1
print(ans - 1)