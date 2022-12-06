f = lambda: int(input())

N = f()
S = input()
a = S.count('C')
print(N // (N - a + 1))