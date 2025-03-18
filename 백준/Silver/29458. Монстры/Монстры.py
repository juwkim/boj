input()
ans, num = "No", 0
for a in map(int, input().split()):
    if num | a != num + a:
        break
    num |= a
else:
    if num & (num + 1) == 0:
        ans = "Yes"
print(ans)