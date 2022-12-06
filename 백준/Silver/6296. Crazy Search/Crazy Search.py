N, NC = map(int, input().split())
s = input()
ans = len(set(s[i:i+N] for i in range(len(s)-N+1)))
print(ans)