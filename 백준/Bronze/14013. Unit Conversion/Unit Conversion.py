x, y = map(float, input().split())
product = {'A': y/x, 'B': x/y}
for _ in range(int(input())):
    command = input()
    print(float(command[:-1]) * product[command[-1]])