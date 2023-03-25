g = lambda: [*map(int, input().split())]

n = int(input())
ans = 'YES'
Sum = 0
for num in g()[:-1]:
    Sum += num
    if Sum <= 0:
        ans = 'NO'
        break
print(ans)