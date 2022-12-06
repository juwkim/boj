N = int(input())
array = [[*map(int, input().split())] for _ in range(N)]
white, blue = 0, 0
def solve(array, x, y, size):
    global white, blue
    if size == 1:
        if array[x][y]:
            blue += 1
        else:
            white += 1
        return;
    
    total = sum(sum(array[i][y:y+size]) for i in range(x, x+size))
    if total == size**2:
        blue += 1
    elif total == 0:
        white += 1
    else:
        size //= 2
        solve(array, x, y, size)
        solve(array, x+size, y, size)
        solve(array, x, y+size, size)
        solve(array, x+size, y+size, size)

solve(array, 0, 0, N)
print(white, blue, sep='\n')