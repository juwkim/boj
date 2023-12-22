import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    print(input())
    cnt, address = input().split()
    print(cnt, address)
    
    check = [0] * 10
    cnt = int(cnt)
    while cnt:
        s = input()
        if s[0] == '+':
            _, *l = s.split()
            start, stop, step = map(int, l)
            for i in range(start, stop + 1, step):
                num = i
                while num:
                    check[num % 10] += 1
                    num //= 10
            cnt -= (stop - start) // step + 1
        else:
            num = int(s)
            while num:
                check[num % 10] += 1
                num //= 10
            cnt -= 1
    for idx, val in enumerate(check):
        print(f"Make {val} digit {idx}")
    total = sum(check)
    print(f"In total {total} digit{'' if total == 1 else 's'}")