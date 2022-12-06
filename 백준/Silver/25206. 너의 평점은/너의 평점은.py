score = lambda x: 69 - ord(x[0]) + 0.5 * (x[1] == '+') 
cnt = 0
Sum = 0
for _ in range(20):
    name, credit, grade = input().split()
    credit = float(credit)
    if grade != 'P':
        cnt += credit
        if grade != 'F':
            Sum += credit * score(grade)
print(Sum / cnt)