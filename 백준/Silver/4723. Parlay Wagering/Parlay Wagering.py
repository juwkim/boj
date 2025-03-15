import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    money, n = map(int, input().split())
    money *= 100
    for odd, res in [input().split() for _ in range(n)]:
        odd = int(odd)
        match res[0]:
            case 'W':
                if odd > 0:
                    odd *= 10
                else:
                    odd = 100000 // -odd
                money += money * odd // 1000
            case 'L':
                money = 0
                break
            case 'T':
                continue
        if money >= 100000000:
            money = 100000000
            break
    q, r = divmod(money, 100)
    print(f"${q:,}.{r:02d}")