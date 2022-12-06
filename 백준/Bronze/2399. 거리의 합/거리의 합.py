N = int(input())
k = sorted(map(int, input().split()))
now = sum(i - k[0] for i in k[1:])
total = now
for i in range(1, N):
    now += (2*i-N) * (k[i] - k[i-1])
    total += now
print(total)