start = float(input())
while True:
    last = float(input())
    if last == 999:
        break
    print("%.2f" % (last - start))
    start = last