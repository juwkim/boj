def g(): return [*map(int, input().split())]

boy, girl = [], []
for _ in range(int(input())):
    a, h = g()
    if a:
        girl.append(h)
    else:
        boy.append(h)
boy.sort()
girl.sort()

students = girl + boy
print(max(abs(a - b) for a, b in zip(students, students[1:])))