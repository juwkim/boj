g = lambda x, a, b: x.replace(a, b)
h = lambda: g(g(g(g(g(g(g(input(), '%', '%25'), '!', '%21'), '$', '%24'),
                      ' ', '%20'), '(', '%28'), ')', '%29'), '*', '%2a')
while (s:=h()) != '#':
    print(s)