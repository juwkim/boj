a = 1
while True:
    print("? A", a, flush=True)
    if input() == '1':
        break
    a += 1
b = 1
while True:
    print("? B", b, flush=True)
    if input() == '1':
        break
    b += 1
print("!", a + b, flush=True)