for i in range(1, 1 + int(input())):
    N = int(input())
    while True:
        digits = [i for i in str(N)]
        if all(digits[i] <= digits[i+1] for i in range(len(digits)-1)):
            break
        N -= 1
    print(f'Case #{i}: {N}')