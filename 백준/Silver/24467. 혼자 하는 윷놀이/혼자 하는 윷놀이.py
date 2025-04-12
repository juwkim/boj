ans = "LOSE"
x, d = 0, 0
for _ in range(10):
    while True:
        cnt = input().count('0')
        if cnt == 0: cnt = 5
        match d:
            case 0:
                if x + cnt == 5:
                    x, d = 0, 3
                elif x + cnt > 5:
                    x, d = x + cnt - 5, 1
                else:
                    x, d = x + cnt, 0
            case 1:
                if x + cnt == 5:
                    x, d = 0, 4
                elif x + cnt > 5:
                    x, d = x + cnt - 5, 2
                else:
                    x, d = x + cnt, 1
            case 2:
                x += cnt
                if x > 10:
                    ans = "WIN"
                    break
            case 3:
                if x + cnt == 3:
                    x, d = 3, 4
                elif x + cnt > 5:
                    x, d = x + cnt - 1, 2
                else:
                    x, d = x + cnt, 3
            case 4:
                x += cnt
                if x > 6:
                    ans = "WIN"
                    break
        if 0 < cnt < 4:
            break
    if ans == "WIN":
        break
print(ans)