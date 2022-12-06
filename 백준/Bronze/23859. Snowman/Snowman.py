s = input()
n = int(input())

ans = 'zz'
for i in range(len(s)-1):
    p = s[i:i+2]
    ans = min(ans, p, p[::-1])
        
print(ans * (n >> 1) + ans[0] * (n & 1))