piano = 'A BC D EF G '
piano_len = len(piano)

n = int(input())
nums = [int(input()) for _ in range(n)]
for cur in [0, 2, 3, 5, 7, 8, 10]:
    ans = piano[cur]
    flag = True
    for i in range(n):
        cur = (cur + nums[i]) % piano_len
        now = piano[cur]
        if not now.isalpha():
            flag = False
            break
    if flag:
        print(ans, now)