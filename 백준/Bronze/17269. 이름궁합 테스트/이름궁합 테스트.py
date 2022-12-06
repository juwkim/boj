table = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3,
         'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2,
         'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2,
         'Y': 2, 'Z': 1}    

N, M = map(int, input().split())
A, B = map(lambda s: [table[i] for i in s], input().split())

temp = []
for i in range(min(N, M)):
    temp += [A[i], B[i]]

if N > M:
    temp += A[M:]
elif N < M:
    temp += B[N:]

while len(temp) != 2:
    save = []
    for i in range(len(temp) - 1):
        save.append((temp[i] + temp[i+1]) % 10)
    temp = save

print(f'{temp[0] * 10 + temp[1]}%')