N = int(input())
print('*'.rjust(N))
for i in range(N - 2):
    print(('*' + ' ' * (2 * i + 1) + '*').rjust(N + i + 1))
if N > 1:
    print('*' * (2 * N - 1))