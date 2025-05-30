import sys
input = sys.stdin.readline

MAX = 2_000_000
is_prime = [False, False] + [True] * (MAX - 1)
for i in range(2, int(MAX**.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

for _ in range(int(input())):
    N = int(input())
    A = 3
    while not is_prime[A] or not is_prime[2 * N - A]:
        A += 2
    print(A, 2 * N - A)