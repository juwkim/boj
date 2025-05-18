import sys
input = sys.stdin.readline

def base36(n):
    if n < 10:
        return str(n)
    else:
        return chr(n + 55)

while (l:=input())[0] != '0':
    N, M, Q = map(int, l.split())
    S_list, B_list = [], []
    for _ in range(Q):
        S, B = input().split()
        S_list.append(list(map(int, S)))
        B_list.append(list(map(int, B)))
    result = []
    for bulb in range(M):
        ans = -1
        for switch in range(N):
            state, valid = 0, True
            for q in range(Q):
                state ^= S_list[q][switch]
                if state != B_list[q][bulb]:
                    valid = False
                    break
            if valid:
                if ans == -1:
                    ans = switch
                else:
                    ans = -1
                    break
        if ans == -1:
            result.append('?')
        else:
            result.append(base36(ans))
    print(''.join(result))