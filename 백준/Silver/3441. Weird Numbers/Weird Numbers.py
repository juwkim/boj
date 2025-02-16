import sys
input = sys.stdin.readline

while (s:=input())[0] != 'e':
    a, b = s.split()
    if a[0] == 't':
        base, num = int(a[2:]), int(b)
        ans = []
        while True:
            num, r = divmod(num, base)
            if r < 0:
                r += -base
                num += 1
            ans.append(r)
            if num == 0:
                break
        print(*ans[::-1], sep='')
    else:
        num, base = 0, int(a[4:])
        for c in b:
            num = num * base + int(c)
        print(num)