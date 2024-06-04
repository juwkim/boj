import sys
input = sys.stdin.readline

def identity():
    global id
    for i in range(1, N + 1):
        if all(a[i][j] == a[j][i] == j for j in range(1, N + 1)):
            id = i
            return True
    return False

def inverse():
    for i in range(1, N + 1):
        if all(a[i][j] != id or a[j][i] != id for j in range(1, N + 1)):
            return False
    return True

def associatuve():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if a[i][a[j][k]] != a[a[i][j]][k]:
                    return False
    return True

while N:=int(input()):
    id = -1
    a = [[0] * (N + 1)] + [[0] + [*map(int, input().split())] for _ in range(N)]
    if identity() and inverse() and associatuve():
        print("yes")
    else:
        print("no")