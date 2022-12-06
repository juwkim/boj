import sys
myset = [0]*21
for i in range(int(sys.stdin.readline())):
    commands = sys.stdin.readline().split()
    command = commands[0]
    if len(commands) == 2:
        num = int(commands[1])
        
    if command == 'add':
        myset[num] = 1
    elif command == 'remove':
        myset[num] = 0
    elif command == 'check':
        print(myset[num])
    elif command == 'toggle':
        myset[num] = 1 - myset[num]
    elif command == 'all':
        myset = [1]*21
    else:
        myset = [0]*21