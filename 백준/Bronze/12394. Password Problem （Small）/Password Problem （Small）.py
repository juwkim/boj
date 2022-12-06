import sys
I = sys.stdin.readline
for i in range(1, 1 + int(I())):
    A, B = map(int, I().split())
    p = [*map(float, I().split())]
    
    table = [1]
    for j in range(A):
        table.append(table[-1] * p[j])
        table[j] *= 1 - p[j]
        
    a = (2*B - A + 2) - (B + 1) * table[-1]
    b = B + 2
    c = min(sum(table[j] * (B - A + 2 * i + 3 + (B + 1) * (j < A - 1 - i)) for j in range(A+1)) for i in range(A))
    print(f'Case #{i}: {min(a, b, c)}')