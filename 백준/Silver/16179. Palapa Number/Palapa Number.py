for _ in range(int(input())):
    print(5625 * pow(10, int(input()) - 4, 9973) % 9973)