total = 0
mul = None
for idx, c in enumerate(input()):
    if c == '?':
        mul = 10 - idx
    elif c == 'X':
        total += (10 - idx) * 10
    else:
        total += (10 - idx) * int(c)
ans = -1
for num in range(0, 10 * mul, mul):
    if (total + num) % 11 == 0:
        ans = num // mul
        break
if mul == 1 and (total + 10 * mul) % 11 == 0:
    ans = 'X'
print(ans)