N = int(input())
ans = 1
while(True):
    if N > 1 + 3 * ans * (ans - 1):
        ans += 1
    else:
        break
print(ans)