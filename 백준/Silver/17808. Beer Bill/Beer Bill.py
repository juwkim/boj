ans = 0
while True:
    try:
        line = input().rstrip()
        if line[0] == '|':
            ans += 42 * len(line)
        else:
            a, b = line.split(',-')
            ans += int(a) * len(b)
    except:
        break
print("{},-".format((ans + 9) // 10 * 10))