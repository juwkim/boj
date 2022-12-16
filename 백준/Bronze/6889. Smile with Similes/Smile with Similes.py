n = int(input())
m = int(input())
A = [input() for _ in range(n)]
for _ in range(m):
    s = input()
    for t in A:
        print(f'{t} as {s}')