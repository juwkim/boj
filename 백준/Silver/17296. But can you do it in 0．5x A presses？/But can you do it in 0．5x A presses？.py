N = int(input())
ans, pressed = 0, False
for num in input().split():
    if num == '0':
        continue
    idx = num.find('.')
    if idx == -1:
        ans += int(num)
        pressed = True
    elif pressed:
        ans += int(num[:idx])
    else:
        ans += int(num[:idx]) + 1
        pressed = True
print(ans)