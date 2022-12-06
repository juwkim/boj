n = int(input())
bats = [*map(int, input().split())]
print(sum(filter(lambda x: x * (x != -1), bats)) / (n - bats.count(-1)))