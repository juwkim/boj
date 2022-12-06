K, N = map(int, [input(), input()])
for i in range(1, N):
    print(i)
print(K - N*(N-1)//2)