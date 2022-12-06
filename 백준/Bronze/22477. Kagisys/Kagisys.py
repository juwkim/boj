msg = ['Closed', 'Opened']
state = 1
user = {input() for _ in range(int(input()))}
for _ in range(int(input())):
    a = input()
    if a in user:
        print(msg[state], 'by', a)
        state ^= 1
    else:
        print('Unknown', a)