A = [1, 1]
N = int(input())
for i in range(2, N + 1):
    num = 1
    while any(num + A[i - 2 * k] == 2 * A[i - k] for k in range(1, i // 2 + 1)):
        num += 1
    A.append(num)
print(A[-1])