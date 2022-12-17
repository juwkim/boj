dic = {'Paper': 57.99, 'Printer': 120.50, 'Planners': 31.25, 'Binders': 22.50, 'Calendar': 10.95, 'Notebooks': 11.20, 'Ink': 66.95}
ans = 0
while (s:= input()) != 'EOI':
    ans += dic[s]
print("$%.2f" % ans)