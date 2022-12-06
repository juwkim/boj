for _ in range(int(input())):
    s = input()
    print(eval(s) if '+' in s else 'skipped')