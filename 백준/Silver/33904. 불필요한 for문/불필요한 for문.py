*lines, last = open(0).read().splitlines()
variables = []
for line in lines[::-1]:
    v = line.split()[-1][:-3]
    if v in last and v not in variables:
        variables.insert(0, v)
for i in range(len(variables)):
    v = variables[i]
    print(' ' * i + f"for (int {v} = 1; {v} < 9; {v}++)")
print(' ' * len(variables) + last.strip())