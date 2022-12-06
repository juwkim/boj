k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())
p = max(0, k - a) * x + max(0, k - a - b) * y
q = max(0, k - a - b) * x + max(0, k - b) * y
print(max(p, q))