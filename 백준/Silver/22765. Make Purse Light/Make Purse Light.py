import sys
input = sys.stdin.readline

while cost := int(input()):
    a, b, c, d = map(int, input().split())
    money = a * 10 + b * 50 + c * 100 + d * 500
    change = money - cost
    l, change = divmod(change, 500)
    k, change = divmod(change, 100)
    j, change = divmod(change, 50)
    i = change // 10
    for num, change_cnt, original_cnt in zip((10, 50, 100, 500), (i, j, k, l), (a, b, c, d)):
        if original_cnt > change_cnt:
            print(num, original_cnt - change_cnt)
    print()