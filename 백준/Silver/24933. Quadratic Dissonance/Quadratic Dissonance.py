A, B, C, D = map(int, input().split())

def get_val(a1, a2, x):
    return x * x + a1 * x + a2
    
if A == C:
    x = -A / 2
    h = get_val(A, max(B, D), x)
    print(x, h)
else:
    cross = (D - B) / (A - C)
    if min(-A / 2, -C / 2) < cross < max(-A / 2, -C / 2):
        x = cross
        h = get_val(A, B, x)
    else:
        x1, x2 = -A / 2, -C / 2
        h1, h2 = get_val(A, B, x1), get_val(C, D, x2)
        if h1 > h2:
            x, h = x1, h1
        else:
            x, h = x2, h2
    print(x, h)