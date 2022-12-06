p = lambda x, y, z: x < y >= z
q = lambda x, y, z: x > y <= z
r = lambda x, y, z: (x == y) and (y != z)
N = int(input())
a, b, c = [int(input()) for _ in range(3)]
s, t = a, b
Max, Min, plane = p(a, b, c), q(a, b, c), r(a, b, c)
for _ in range(N-3):
    a, b, c = b, c, int(input())
    Max += p(a, b, c)
    Min += q(a, b, c)
    plane += r(a, b, c)

Max += p(b, c, s) + (c < s)
Min += q(b, c, s) + (c > s)
plane += ((a != b) and b == c) + (c == s)
print(plane, Max, Min)