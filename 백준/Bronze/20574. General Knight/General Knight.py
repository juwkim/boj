def solve(x_move, y_move):
    global cnt
    p = chr(ord(x) + x_move)
    q = int(y) + y_move
    if 'a' <= p <= 'h' and 1 <= q <= 8:
        if p + str(q) not in buf:
            cnt += 1
            buf.append(p + str(q))
a, b = sorted(map(int, input().split()))
x, y = [*input()]
cnt = 0
buf = []

solve(-b, -a)
solve(-b, a)
solve(-a, -b)
solve(-a, b)
solve(a, -b)
solve(a, b)
solve(b, -a)
solve(b, a)

print(cnt)
print(*buf)