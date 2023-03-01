log = bytearray(1001)
input()
ans = 0
for num in map(int, input().split()):
    if num > 0:
        log[num] = 1
    else:
        ans += log[-num] == 0
        log[-num] = 0
print(ans)