N = int(input())
time = 0
for i, t in enumerate(sorted(map(int, input().split()))):
    time += (N - i) * t
print(time)