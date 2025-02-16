import sys
input = sys.stdin.readline
check = lambda a, b, cur: all(a <= rank <= b for rank, _, _ in cur) and all(s <= i <= t for _, s, t in cur)
ans, cur = 0, []
for i in range(1, 1 + int(input())):
    a, b = map(int, input().split())
    match len(cur):
        case 0:
            cur = [(i, a, b)]
        case 1:
            if check(a, b, cur):
                cur.append((i, a, b))
            else:
                cur = [(i, a, b)]
        case 2:
            if check(a, b, cur):
                ans += 1
                cur = []
            else:
                cur.pop(0)
                if check(a, b, cur):
                    cur.append((i, a, b))
                else:
                    cur = [(i, a, b)]
print(ans)