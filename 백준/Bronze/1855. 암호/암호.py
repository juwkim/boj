N = int(input())
S = input()
a = [S[i:i+N][::1 - i //N % 2 * 2] for i in range(0, len(S), N)]
print(*[''.join([sub[i] for sub in a]) for i in range(N)], sep="")