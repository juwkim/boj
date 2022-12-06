while True:
    command = input().split()
    if command == ['0', 'W', '0']:
        break
    if command[1] == 'D':
        print(int(command[0]) + int(command[2]))
    else:
        num = int(command[0]) - int(command[2])
        print(num if num >= -200 else 'Not allowed')