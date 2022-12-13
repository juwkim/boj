Map = [[-1, -1, -1] for _ in range(3)]
N = int(input())
for i in range(N):
    r, c = divmod(int(input()) - 1, 3)
    Map[r][c] = i & 1


if [0, 0, 0] in Map:
    ans = 3
elif [1, 1, 1] in Map:
    ans = 4
else:
    Map = [*zip(*Map)]
    if (0, 0, 0) in Map:
        ans = 3
    elif (1, 1, 1) in Map:
        ans = 4
    elif (Map[0][0], Map[1][1], Map[2][2]) == (0, 0, 0):
        ans = 3
    elif (Map[0][0], Map[1][1], Map[2][2]) == (1, 1, 1):
        ans = 4
    elif (Map[0][2], Map[1][1], Map[2][0]) == (0, 0, 0):
        ans = 3
    elif (Map[0][2], Map[1][1], Map[2][0]) == (1, 1, 1):
        ans = 4
    elif N == 9:
        ans = 5
    elif N & 1:
        ans = 2
    else:
        ans = 1
print(ans)