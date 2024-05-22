N, *A = map(int, open(0).read().split())
def solve(l):
    cnt = 0
    for i in range(N):
        for j in range(N - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                cnt += 1
    return cnt
print(min(1 + solve([N - num for num in A]), solve(A)))