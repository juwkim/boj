def solve(size, x, y):
    if size == 0: return arr[x][y]
    res = "".join(solve(size // 2, p, q) for p, q in ((x, y), (x, y + size), (x + size, y), (x + size, y + size)))
    match res:
        case '0000': return '0'
        case '1111': return '1'
        case _:      return f"({res})"
N = int(input())
arr = [input() for _ in range(N)]
print(solve(N // 2, 0, 0))