N, *H = map(int, open(0))
print(sum(H[i] == H[i - N // 2] for i in range(N)))