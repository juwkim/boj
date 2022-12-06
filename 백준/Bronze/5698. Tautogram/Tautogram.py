while (s := input()) != '*':
    a = {i[0].lower() for i in s.split()}
    print('NY'[len(a) == 1])