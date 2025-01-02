import sys
input = lambda: sys.stdin.readline().rstrip()

while (s:=input()) != '#':
    ans = 0
    while s != '0':
        _, _, num, t = s.split()
        num = int(num)
        if t == 'F':
            ans += 2 * num
        elif t == 'B':
            ans += (3 * num + 1) // 2
        else:
            ans += max(num, 500)
        s = input()
    print(ans)