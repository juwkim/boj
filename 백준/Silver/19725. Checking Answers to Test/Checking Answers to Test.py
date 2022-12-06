n = int(input())
s = input()
m = int(input())
students = [input() for _ in range(m)]
buf = []
for i in range(m-1):
    for j in range(i+1, m):
        same = 0
        same1, correct1 = 0, 0
        same2, correct2 = 0, 0
        
        same3, same4 = 0, 0
        
        for x, y, ans in zip(students[i], students[j], s):
            if x == y:
                if x == ans:
                    same1 += 1
                    correct1 += 1
                    same2 += 1
                    correct2 += 1
                else:
                    same3 += 1
                    same4 += 1
            else:
                if x == ans:
                    correct1 += 1
                if y == ans:
                    correct2 += 1
        if 2 * same1 > correct1 and 2 * same2 > correct2 and 2 * same3 > n - correct1 and 2 * same4 > n - correct2:
            buf.append((i+1, j+1))
print(len(buf))
for l in buf:
    print(*l)