for _ in range(int(input())):
    num = input()
    count = 0
    for i in range(0, 16, 2):
        count += sum(divmod(int(num[i]) * 2, 10)) + int(num[i+1])
    print('F' if count % 10 else 'T')