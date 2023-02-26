def g(): return [*map(int, input().split())]

N, M = g()
S = input()
end = N - 1
while end and S[end] in 'AEIOU':
    end -= 1

start = end
A = 2
while start and A:
    A -= S[start] == 'A'
    start -= 1
if A == 0 and start + 4 >= M:
    print('YES')
    print(S[:M - 3] + 'AA' + S[end])
else:
    print('NO')