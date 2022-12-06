N, P = map(int, input().split())
array, now = [N], N * N % P
while now not in array:
    array += [now]
    now = now * N % P
print(len(array) - array.index(now))