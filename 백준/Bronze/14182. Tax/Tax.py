while True:
    num = int(input())
    if num == 0:
        break
    if num > 5000000:
        num *= 0.8
    elif num > 1000000:
        num *= 0.9
    print(int(num))