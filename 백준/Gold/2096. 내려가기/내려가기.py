input = __import__('sys').stdin.readline

def g(): return [*map(int, input().split())]

N = int(input())
Min = Max = g()
for _ in range(N - 1):
    a, b, c = g()
    p = a + min(Min[0], Min[1])
    q = b + min(Min)
    r = c + min(Min[1], Min[2])
    
    x = a + max(Max[0], Max[1])
    y = b + max(Max)
    z = c + max(Max[1], Max[2])
    
    Min = [p, q, r]
    Max = [x, y, z]
print(max(Max), min(Min))