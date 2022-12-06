T = int(input())
droid = (350.34, 230.90, 190.55, 125.30, 180.90)
for _ in range(T):
    nums = list(map(int, input().split()))
    price = 0
    for i in range(5):
        price += nums[i] * droid[i]
    print('$%.2f' % price)