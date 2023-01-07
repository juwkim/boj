ans = ''
for i in map(str, range(1, 1 + int(input()))):
    if i not in ans:
        ans += i
print(ans)