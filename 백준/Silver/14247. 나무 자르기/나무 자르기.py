g = lambda: map(int, input().split())
input()
print(sum(g()) + sum(i * num for i, num in enumerate(sorted(g()))))