def time():
    h, m = map(int, input().split(':'))
    return h * 60 + m

s, e = time(), time() + 24 * 60
h, m = divmod(e - s, 60)
print(f"{h:02d}:{m:02d}")