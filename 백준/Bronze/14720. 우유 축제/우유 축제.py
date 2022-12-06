input()
milks = [*map(int, input().split())]
total, pos = 0, 0
for milk in milks:
   if milk == pos:
       total += 1
       pos = (pos+1) % 3
print(total)