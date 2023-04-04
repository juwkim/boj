ans = 0
while True:
    try:
        a, b = input().split()
        b = int(b)
        if a == 'Es':
            ans += 21 * b
        else:
            ans += 17 * b
    except:
        break
print(ans)