import sys
input = sys.stdin.readline

for _ in range(int(input())):
    w, l = sorted(map(int, input().split()))
    ans = []
    num = 2 * (w + l - 2)
    for i in range(1, min(w, int(num ** 0.5)) + 1):
        if num % i:
            continue
        prv = -1
        for a in (i, num // i):
            if a == prv:
                continue
            prv = a
            match w % a:
                case 0:
                    if (l - 2) % a == 0 or (a == 2 and (l - 1) % a == 0):
                        ans.append(a)
                case 1:
                    if (l - 1) % a == 0 or (a == 2 and l % a == 0):
                        ans.append(a)
                case 2:
                    if l % a == 0:
                        ans.append(a)
    print(len(ans), *sorted(ans))