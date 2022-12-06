def check(point1, point2):
    if point1 or point2:
        return 1000 * point1**2 // (point1**2 + point2**2)
    else:
        return 0

for _ in range(int(input())):
    n, m = map(int, input().split())
    
    plus = [0 for _ in range(n)]
    minus = [0 for _ in range(n)]
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        
        a -= 1
        b -= 1
        
        plus[a] += p
        plus[b] += q
        
        minus[a] -= q
        minus[b] -= p
        
    results = [check(a, b) for a, b in zip(plus, minus)]
    print(max(results))
    print(min(results))