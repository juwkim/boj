import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    t = 1
    buf = ""
    while (s:=input()) != "END OF CASE":
        while (idx:=s.find(';')) != -1:
            print(f"{t}: {buf + s[:idx + 1]}")
            buf = ""
            s = s[idx + 1:]
        buf += s
        t += 1