n, a = map(int, input().split())
print(sum(num // a for num in map(int, input().split())))