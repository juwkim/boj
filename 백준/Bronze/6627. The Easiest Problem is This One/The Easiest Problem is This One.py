while True:
    num = input()
    if num == '0':
        break
    
    i = 11
    digit_sum = sum(map(int, [digit for digit in num]))
    while True:
        mul_digit_sum = sum(map(int, [digit for digit in str(i * int(num))]))
        if digit_sum == mul_digit_sum:
            break
        i += 1
    print(i)