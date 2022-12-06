N, X = map(int, [input(), input()])
price = 0
for _ in range(N):
    P1, P2 = map(int, input().split())
    if abs(P1-P2) <= X:
        price += max(P1, P2)
    else:
        price += int(input())
print(price)