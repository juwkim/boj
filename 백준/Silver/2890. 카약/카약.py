R, C = map(int, input().split())
arr = [0] * R
for _ in range(R):
    line = input()
    i = 1
    for i in range(1, C-1):
        if line[i] != '.':
            break
    if line[i] != '.':
        arr[int(line[i]) - 1] = i
for num in arr:
    if num:
        print(1 + sum(num < i for i in set(arr)))