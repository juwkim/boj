a, b = map(int, input().split())
n = int(input())
taxi = [list(map(int, input().split())) for _ in range(n)]
print(*min(taxi, key=lambda x: abs(a-x[0])+abs(b-x[1])))