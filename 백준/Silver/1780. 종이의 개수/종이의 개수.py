import sys
input = sys.stdin.readline
N = int(input())
array = [[*map(int, input().split())] for _ in range(N)]
one, zero, minus = 0, 0, 0
def solve(array, x, y, size):
    global one, zero, minus
    if size == 1:
        if array[x][y] == 1:
            one += 1
        elif array[x][y] == 0:
            zero += 1
        else:
            minus += 1
        return;
    
    cone, czero, cminus = 0, 0, 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            if array[i][j] == 1:
                cone += 1
            elif array[i][j] == 0:
                czero += 1
            else:
                cminus += 1

    if cone == size**2:
        one += 1
    elif czero == size**2:
        zero += 1
    elif cminus == size**2:
        minus += 1
    else:
        size //= 3
        solve(array, x, y, size)
        solve(array, x, y+size, size)
        solve(array, x, y+2*size, size)
        solve(array, x+size, y, size)
        solve(array, x+size, y+size, size)
        solve(array, x+size, y+2*size, size)
        solve(array, x+2*size, y, size)
        solve(array, x+2*size, y+size, size)
        solve(array, x+2*size, y+2*size, size)
solve(array, 0, 0, N)
print(minus, zero, one, sep='\n')