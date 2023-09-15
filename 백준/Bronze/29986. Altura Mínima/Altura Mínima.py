N, H = map(int, input().split())
print(sum(H >= num for num in map(int, input().split())))