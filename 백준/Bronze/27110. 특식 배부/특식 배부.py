N = int(input())
ans = sum(min(num, N) for num in map(int, input().split()))
print(ans)