a=[l.split()for l in open(0)]
print(+any(1==len({*x})for x in a+[*zip(*a)]))