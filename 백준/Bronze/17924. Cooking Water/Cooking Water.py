check = [0] * 1001
N = int(input())
for _ in [0]*N:
    a, b = map(int, input().split())
    for i in range(a, b+1):
        check[i] += 1
print('gunilla has a point' if N in check else 'edward is right')