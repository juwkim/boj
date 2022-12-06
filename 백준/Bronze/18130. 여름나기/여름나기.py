N, Q = map(int, input().split())
P, K, C = map(int, input().split())
num = 1
S = (Q - 1) // K
min_cost = P + C * S * (S + 1) // 2

for i in range(2, 1 + N):
    P, K, C = map(int, input().split())
    S = (Q - 1) // K 
    cost = P + C * S * (S + 1) // 2
    if cost < min_cost:
        min_cost = cost
        num = i
print(num, min_cost)