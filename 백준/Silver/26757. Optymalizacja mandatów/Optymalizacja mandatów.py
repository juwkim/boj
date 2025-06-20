N = int(input())
K = list(map(int, input().split()))
R = list(map(int, input().split()))
total = 0
for k, (d, r) in zip(sorted(K, reverse=True), sorted((len(str(r)), r) for r in R)):
    total += k * (10 ** d) + r
print(total)