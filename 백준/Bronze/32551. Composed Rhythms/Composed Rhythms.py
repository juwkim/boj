N = int(input())
if N & 1:
    ans = [3] + [2] * ((N - 3) // 2)
else:
    ans = [2] * (N // 2)

print(len(ans))
print(*ans)