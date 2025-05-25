A, B, C = map(int, input().split())
S, V = map(int, input().split())
left = 100 * (250 - int(input()))
time = 0
get1 = 30 * V * C
if left <= get1:
    time = (left + C - 1) // C
else:
    left -= get1
    time += 30 * V
    get2 = 30 * S * B
    if left <= get2:
        time += (left + B - 1) // B
    else:
        left -= get2
        time += 30 * S
        time += (left + A - 1) // A
print(time)