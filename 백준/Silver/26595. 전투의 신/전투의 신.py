g = lambda: [*map(int, input().split())]

N = int(input())
A, Pa, B, Pb = g()
Max, x, y = 0, 0, 0
for i in range(1 + N // Pa):
    j = (N - i * Pa) // Pb
    num = i * A + j * B
    if num > Max:
        Max = num
        x, y = i, j
print(x, y)