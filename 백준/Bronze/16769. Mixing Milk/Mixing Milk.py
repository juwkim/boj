g = lambda: map(int, input().split())
c1, m1 = g()
c2, m2 = g()
c3, m3 = g()

for _ in range(33):
    a = min(m1, c2-m2)
    m1, m2 = m1 - a, m2 + a
    b = min(m2, c3-m3)
    m2, m3 = m2 - b, m3 + b
    c = min(m3, c1-m1)
    m3, m1 = m3 - c, m1 + c

a = min(m1, c2-m2)
m1, m2 = m1 - a, m2 + a

print(m1, m2, m3)  