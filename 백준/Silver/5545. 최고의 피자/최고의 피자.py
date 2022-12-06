N = int(input())
A, B = map(int, input().split())
C = int(input())
energy, cost = C, A
D_list = sorted([int(input()) for _ in range(N)], reverse=True)
for D in D_list:
    if (energy + D) / (cost + B) < energy / cost:
        break
    energy += D
    cost += B
print(energy // cost)