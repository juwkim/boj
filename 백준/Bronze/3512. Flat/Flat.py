import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]

n, c = g()
room, bedroom, balcony = 0, 0, 0
for _ in range(n):
    size, name = input().split()
    size = int(size)
    room += size
    if name == 'bedroom':
        bedroom += size
    elif name == 'balcony':
        balcony += size
print(room)
print(bedroom)
print((room - balcony / 2) * c)