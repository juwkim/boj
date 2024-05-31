n = int(input())
s = input()
idx = [i for i in range(n - 1) if s[i] != s[i + 1]] + [n - 1]
print(len(idx) // 2)
for i in range(0, len(idx) - 1, 2):
    print(f"{idx[i] + 2}-{idx[i + 1] + 1}")