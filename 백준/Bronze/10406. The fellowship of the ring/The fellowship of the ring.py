W, N, P = map(int, input().split())
print(len([num for num in map(int, input().split()) if W <= num <= N]))