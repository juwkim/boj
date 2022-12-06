i = 1
while l_stride := int(input()):
    print(f'User {i}')
    for _ in range(int(input())):
        print(f'{l_stride * int(input()) / 10**5:.5f}')
    i += 1