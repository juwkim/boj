p1, q1 = map(int, input().split('/'))
b = int(input().split('/')[1])
p2, q2 = map(int, input().split('/'))
s, t = p1 * b // q1 + 1, (p2 * b - 1) // q2
print(-1 if s > t else f"{s}/{b}")