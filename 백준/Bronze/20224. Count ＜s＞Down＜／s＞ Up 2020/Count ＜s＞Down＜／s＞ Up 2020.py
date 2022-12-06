while n:=int(input()):
    num = input()
    print(sum(num[i:i+7] == '2 0 2 0' for i in range(0, 2*n - 7)))