N = int(input())
mailboxes = input()
for K in range(1, N+1):
    if N - K + 1 == len(set(mailboxes[i:i+K] for i in range(N-K+1))):
        print(K)
        break