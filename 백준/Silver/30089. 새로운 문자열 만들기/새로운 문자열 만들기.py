import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    S = input()
    pre = 0
    for i in range(len(S), 0, -1):
        if S[len(S)-i:] == S[len(S)-i:][::-1]:
            pre = i
            break
    ans = S + S[:len(S)-pre][::-1]
    print(ans)