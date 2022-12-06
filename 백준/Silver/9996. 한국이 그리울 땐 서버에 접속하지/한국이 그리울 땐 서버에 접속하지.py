N = int(input())
s, e = input().split('*')
for _ in range(N):
    msg = input()
    if len(msg) >= len(s) + len(e) and msg[:len(s)] == s and msg[-len(e):] == e:
        print('DA')
    else:
        print('NE')