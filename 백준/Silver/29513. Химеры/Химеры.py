a, b = map(int, input().split())
print(sum(i in {1, 3, 9, 11, 33, 99} for i in range(a, b + 1)))