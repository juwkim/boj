while True:
    N = int(input())
    if N == 0:
        break
    Mary = input().count('0')
    print(f'Mary won {Mary} times and John won {N-Mary} times')