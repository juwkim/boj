step = 1
while N:= int(input()):
    ans, div = 0, 5
    while p := (N // div):
        ans += p
        div *= 5
    print(f'Case #{step}: {ans}')
    step += 1