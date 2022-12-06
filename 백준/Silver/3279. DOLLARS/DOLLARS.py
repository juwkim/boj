n = int(input())
a, b = 100, 0
Cur = int(input())
for _ in range(n-1):
    Next = int(input())
    
    if Cur > Next:
        if a:
            b = Cur * a / 100
            a = 0
    elif Cur < Next:
        if b:
            a = b / Cur * 100
            b = 0
    Cur = Next

if b:
    a = b / Cur * 100
print(a)