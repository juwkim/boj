import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    S = input()
    num, cnt = 0, 0
    ans = []
    for i in range(len(S)):
        if S[i] == 'U':
            if cnt:
                ans.append(')')
                cnt -= 1
            else:
                ans.append('(')
                cnt += 1
            num += 1
        elif cnt == len(S) - i:
            ans.append(')')
            cnt -= 1
            num += 2
        else:
            ans.append('(')
            cnt += 1
    print(num)
    print(*ans, sep='')