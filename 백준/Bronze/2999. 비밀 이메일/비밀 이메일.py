def findRC(N):
    S = int(N**.5)
    for i in range(S, 0, -1):
        if N / i == N // i:
            return i, N // i

message = input()
N = len(message)
R, C = findRC(N)

deciphered = ''
for i in range(R):
    for j in range(0, N, R):
        deciphered += message[i + j]
print(deciphered)