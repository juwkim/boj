a = [*map(int, input().split())]
res = 1

if any(s % 2 for s in a):
    for s in a:
        if s % 2:
            res *= s
else:
    for s in a:
        res *= s
        
print(res)