S = [i for i in input()]
for _ in range(int(input())):
    A, B = map(int, input().split())
    S[A], S[B] = S[B], S[A]
print(''.join(S))