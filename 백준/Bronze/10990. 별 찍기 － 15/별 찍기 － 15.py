N = int(input())
print('*'.rjust(N))
for i in range(1, N):
    print(('*' + ' ' * (2 * i - 1) + '*').rjust(N + i))