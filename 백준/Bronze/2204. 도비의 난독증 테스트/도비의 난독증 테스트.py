while n:= int(input()):
    print(min([input() for _ in range(n)], key=str.lower))