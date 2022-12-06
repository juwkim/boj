g = lambda: map(int, input().split())
R, C = g()
A, B = g()

for i in range(R):
    a = (('X' * B + '.' *B) * (C//2))[::(-1)**i] + 'X.'[i%2] * B * (C%2)
    print('\n'.join([a for _ in range(A)]))