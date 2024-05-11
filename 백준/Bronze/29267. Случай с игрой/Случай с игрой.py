save, cur = 0, 0
n, k = map(int, input().split())
for _ in range(n):
    match input():
        case "ammo":
            print(cur := cur + k)
        case "save":
            save = cur
            print(cur)
        case "shoot":
            print(cur := max(0, cur - 1))
        case "load":
            print(cur := save)