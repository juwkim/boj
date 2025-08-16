import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    a, b, x, m, n = map(int, input().split())
    rows = [[0] * 6 for _ in range(n + 1)]
    for r in range(1, n + 1):
        for c in range(1, 6):
            rows[r][c] = (a * rows[r-1][c] + b * rows[r][c-1] + x) % m
    print(f"Case #{tc}:")
    for _ in range(int(input())):
        cmd, *args = input().split()
        args = [0] + [*map(int, args)]
        match cmd:
            case "insert":
                rows.append(args)
            case "remove":
                r = args[1]
                if 1 <= r < len(rows):
                    rows[r] = None
            case "max":
                c = args[1]
                print(max(row[c] for row in rows[1:] if row is not None))
            case "min":
                c = args[1]
                print(min(row[c] for row in rows[1:] if row is not None))
            case "range":
                _, c, lo, hi = args
                print(sum(lo <= row[c] <= hi for row in rows[1:] if row is not None))