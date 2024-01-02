import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve(line: list[int], L: int) -> bool:
    cur, cnt = None, 0
    idx = 0
    while idx < len(line):
        if cur == None:
            cur = line[idx]
            cnt = 1
        elif cur == line[idx]:
            cnt += 1
        elif cur + 1 == line[idx]:
            if cnt < L:
                return False
            cur, cnt = line[idx], 1
        elif cur - 1 == line[idx]:
            if len(line) < idx + L:
                return False
            if any(num != line[idx] for num in line[idx+1:idx+L]):
                return False
            idx += L - 1
            cur, cnt = line[idx], 0
        else:
            return False
        idx += 1
    return True

N, L = g()
Map = [g() for _ in range(N)]
ans = sum(solve(line, L) for line in Map)
Map = list(zip(*Map))
ans += sum(solve(line, L) for line in Map)
print(ans)