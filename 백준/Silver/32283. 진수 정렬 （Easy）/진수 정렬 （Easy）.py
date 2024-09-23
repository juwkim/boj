N, S = int(input()), input()
P = []
for i in range(1 << N):
    num = bin(i)[2:]
    P.append('0' * (N - len(num)) + num)
print(sorted(P, key=lambda x: (x.count('1'), x[::-1])).index(S))