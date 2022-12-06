n = int(input())
Sum = 0
for num in sorted(map(int, input().split())):
    if num > Sum + 1:
        break
    Sum += num
print(Sum + 1)