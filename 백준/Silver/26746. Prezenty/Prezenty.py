N = int(input())
print(N + 1 >> 1)
s = ""
if N & 1:
    s = f"1 {N}"
    N -= 1
for i in range(N >> 1):
    print(2, i + 1, N - i)
if s:
    print(s)