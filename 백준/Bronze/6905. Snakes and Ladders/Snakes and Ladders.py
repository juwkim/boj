dic = {54: 19, 90: 48, 99: 77, 9: 34, 40: 64, 67: 86}
cur = 1
while True:
    num = int(input())
    if num == 0:
        print('You Quit!')
        break
    if cur + num <= 100:
        cur += num
        if cur in dic:
            cur = dic[cur]
    print("You are now on square", cur)
    if cur == 100:
        print('You Win!')
        break