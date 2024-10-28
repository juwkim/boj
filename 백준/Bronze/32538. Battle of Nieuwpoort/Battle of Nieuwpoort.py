def to_base(num, base):
    s = []
    while True:
        num, r = divmod(num, base)
        s.append("0123456789abcdef"[r])
        if num == 0:
            break
    return "".join(s[::-1])

y = int(input().split()[0])
ans = "impossible"
for i in range(2, 17):
    num = to_base(y, i)
    if num[-2:] == "00":
        ans = f"{i} {num}"
        break
print(ans)