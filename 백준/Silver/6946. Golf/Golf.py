from collections import deque

def solve():
    d, n, *clubs = map(int, open(0))
    visited = bytearray(d + 1)
    visited[0] = True
    dq = deque([(0, 0)])
    while dq:
        cur, strokes = dq.popleft()
        for c in clubs:
            nxt = cur + c
            if nxt > d:
                continue
            if nxt == d:
                return f"Roberta wins in {strokes + 1} strokes."
            if not visited[nxt]:
                visited[nxt] = True
                dq.append((nxt, strokes + 1))
    return "Roberta acknowledges defeat."

print(solve())