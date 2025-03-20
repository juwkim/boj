import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, h, m = map(int, input().split())
    if h == -1:
        if m == -1:
            ans = 0
            for i in range(60):
                if a <= b:
                    if a <= i <= b:
                        continue
                elif i >= a or i <= b:
                    continue
                r = i % 5
                for j in range(r * 12, (r + 1) * 12):
                    if a <= b:
                        ans += j < a or b < j
                    elif b < j < a:
                        ans += 1
        else:
            ans = 0
            for i in range(m // 12, 60, 5):
                if a <= b:
                    ans += i < a or b < i
                elif b < i < a:
                    ans += 1
    elif m == -1:
        r = h % 5
        ans = 0
        for i in range(r * 12, (r + 1) * 12):
            if a <= b:
                ans += i < a or b < i
            elif b < i < a:
                ans += 1
    else:
        ans = 1
    print(ans)