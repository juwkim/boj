for _ in [0]*int(input()):
    n = int(input())
    facto = 1
    for i in range(1, n+1):
        facto *= i
        k = 1
        while str(facto)[-k] == '0':
            k += 1
        facto //= pow(10, k-1)

    print(str(facto)[-1])