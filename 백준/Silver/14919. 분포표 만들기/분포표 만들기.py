import decimal
import sys
input = sys.stdin.readline

s = input()
check = [0] * int(s)

m = decimal.Decimal(s)
for num in map(decimal.Decimal, input().split()):
    check[int(num * m)] += 1
print(*check)