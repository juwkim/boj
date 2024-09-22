N = int(input())
ans = "long long"
if -1 << 15 <= N < 1 << 15: ans = "short"
elif -1 << 31 <= N < 1 << 31: ans = "int"
print(ans)