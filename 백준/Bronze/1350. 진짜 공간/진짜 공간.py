input()
files = [*map(int, input().split())]
cluster = int(input())
print(cluster * sum((file - 1) // cluster + 1 for file in files))