moneys = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
checks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(int(input())):
    checks[int(input()) - 1] = 0

offer = int(input())
left = [money for money, check in zip(moneys, checks) if check]
if offer > sum(left) / len(left):
    print("deal")
else:
    print("no deal")