g = lambda: [*map(int, input().split())]
f = lambda: int(input())

ans = 'Wa-pa-pa-pa-pa-pa-pow!'
if f() != 3 or sorted(sorted(g()) for _ in range(3)) != [[1, 3], [1, 4], [3, 4]]:
    ans = 'Woof-meow-tweet-squeek'
print(ans)