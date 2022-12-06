N = int(input())
msg = input()
s = msg.count('s')
t = N - s

for i in range(N):
    if s == t:
        print(msg[i:])
        break
    if msg[i] == 's':
        s -= 1
    else:
        t -= 1