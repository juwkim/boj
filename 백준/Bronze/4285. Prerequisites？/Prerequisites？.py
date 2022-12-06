while (s:=input()) != '0':
    m = int(s.split()[1])
    subject = {*input().split()}
    flag = 1
    categories = [input() for _ in range(m)]
    for category in categories:
        c, r, *course = category.split()
        if len(subject & {*course}) < int(r):
            flag = 0
            break
    print('yes' if flag else 'no')