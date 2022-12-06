N, K = map(int, input().split())
s, t = K % 10, 2 * K % 10
save = []

for i in range(1, N + 1):
    if i % 10 != s and i % 10 != t:
        save += [i]
print(len(save), *save)