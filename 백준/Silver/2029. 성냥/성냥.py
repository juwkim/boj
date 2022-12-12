A = 0 
buf = [input() for _ in range(10)]
for i in range(10):
    if i % 3:
        A += buf[i].count('.') - 6
    else:
        A += buf[i].count('.')
A >>= 1

B = 0
for i in range(1, 10, 3):
    for j in range(1, 10, 3):
        B += buf[i-1][j] + buf[i][j-1] + buf[i+2][j] + buf[i][j+2] == '-|-|'

for i in range(1, 7, 3):
    for j in range(1, 7, 3):
        B += buf[i-1][j:j+5] == '--+--' and buf[i+5][j:j+5] == '--+--' and buf[i][j-1] + buf[i][j+5] + buf[i+3][j-1] + buf[i+3][j+5] == '||||'
B += buf[0] == buf[-1] == '+--+--+--+' and buf[1][0] + buf[4][0] + buf[7][0] + buf[1][-1] + buf[4][-1] + buf[7][-1] == '||||||'
print(A, B)