import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = input()
    l = s.count('-')
    if len(s) - l != 10 or s.startswith('-') or s.endswith('-') or '--' in s or 'X' in s[:-1] or l > 3 or (l == 3 and s[-2] != '-'):
        print('invalid')
        continue
    checksum, i = 0, 10
    for c in s:
        if c.isdigit():
            checksum += int(c) * i
            i -= 1
        elif c == 'X':
            checksum += 10 * i
            i -= 1
    if checksum % 11:
        print('invalid')
        continue
    ans = f'978-{s[:-1]}'
    checksum, f = 0, 0
    for c in ans:
        if c.isdigit():
            checksum += int(c) * (1, 3)[f]
            f ^= 1
        elif c == 'X':
            checksum += 10 * (1, 3)[f]
            f ^= 1
    ans += str((10 - checksum % 10) % 10)
    print(ans)