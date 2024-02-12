n = int(input()) - 1
while True:
    r = n % 4
    print(r, flush=True)
    s = input()
    if s == "I give up":
        break
    n -= r + int(s)