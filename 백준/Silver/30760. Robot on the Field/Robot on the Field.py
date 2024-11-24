def find(c, cnt):
    for i, p in enumerate(s, 1):
        if c == p:
            cnt -= 1
            if cnt == 0:
                return i
    return -1

def solve():
    L, R, U, D = 0, 0, 0, 0
    if x < 0:
        if (L:=find('L', -x)) == -1: return -1
    elif x > 0:
        if (R:=find('R', x)) == -1: return -1
    if y < 0:
        if (D:=find('D', -y)) == -1: return -1
    elif y > 0:
        if (U:=find('U', y)) == -1: return -1
    return f"{L} {U} {R} {D}"

input()
s = input()
x, y = map(int, input().split())
print(solve())