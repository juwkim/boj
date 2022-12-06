g = lambda: [*map(int, input().split())]

step = 1
while n:= int(input()):
    items = []
    
    cnt = n
    while cnt:
        buf = input().split()
        items.extend(buf)
        cnt -= len(buf)
    s_items = sorted(range(n), key=lambda x: items[x])
    print(f'Site {step}:', sum(abs(s_items[i] - i) for i in range(n)))
    step += 1   