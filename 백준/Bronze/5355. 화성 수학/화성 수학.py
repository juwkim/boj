k = {'@': '*3','%': '+5','#': '-7'}
for _ in range(int(input())):
    s = input().split()
    n = float(s[0])
    for op in s[1:]:
      n = eval(str(n) + k[op])  
    print(f"{n:#.2f}")