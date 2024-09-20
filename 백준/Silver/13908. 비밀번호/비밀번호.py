n, m = map(int, input().split())
if m:
    nums = set(input().split())
    print(sum(nums.issubset(set(str(i).zfill(n))) for i in range(10 ** n)))
else:
    print(10 ** n)