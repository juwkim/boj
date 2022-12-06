for _ in range(int(input())):
    i = 0
    num = [*input()]
    while num != [*'6174']:
        i += 1
        
        min_num = ''.join(sorted(num))
        max_num = min_num[::-1]
        num = [*str(int(max_num) - int(min_num))]
        num = ['0' for _ in range(4 - len(num))] + num
    print(i)