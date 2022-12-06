g = lambda: map(int, input().split())
for _ in range(int(input())):
    input()
    print(sum(a != b for a, b in zip(g(), g())))