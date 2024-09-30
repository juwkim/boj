nums = sorted([[*map(int, input().split())] for _ in range(int(input()))], key=sum, reverse=True)
print(sum((x, -y)[i&1] for i, (x, y) in enumerate(nums)))