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
    A = 2
    while True:
        B = 2 * N - A
        if is_prime[A] and is_prime[B]:
            print(A, B)
            break
        A = (A + 2, 3)[A == 2]