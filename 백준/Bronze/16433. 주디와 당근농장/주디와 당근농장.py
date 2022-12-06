N, R, C = map(int, input().split())
s = '.v' * (N // 2) + '.' * (N % 2)
t =  'v.' * (N // 2) + 'v' * (N % 2)
for i in range(N):
    print(s if (R+C+i) % 2 else t)