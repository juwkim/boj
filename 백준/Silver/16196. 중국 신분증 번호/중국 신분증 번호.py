from datetime import date
def solve():
    s = input()
    if s[:6] not in [input() for _ in range(int(input()))]:
        return 'I'
    yyyy, mm, dd = int(s[6:10]), int(s[10:12]), int(s[12:14])
    try:
        d = date(yyyy, mm, dd)
    except:
        return 'I'
    if d < date(1900, 1, 1) or d > date(2011, 12, 31):
        return 'I'
    code = s[14:17]
    if code == "000":
        return 'I'
    num = 0
    for i in range(18):
        if i == 17 and s[i] == 'X':
            c = 10
        else:
            c = int(s[i])
        num = ((num << 1) + c) % 11
    if num == 1:
        return "FM"[int(code) & 1]
    return 'I'
print(solve())