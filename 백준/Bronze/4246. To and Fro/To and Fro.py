while (n:= int(input())):
    s = input().rstrip()
    s = [s[i:i+n][::1 - (i // n) % 2 * 2] for i in range(0, len(s), n)]
    print(*map(''.join, zip(*s)), sep='')