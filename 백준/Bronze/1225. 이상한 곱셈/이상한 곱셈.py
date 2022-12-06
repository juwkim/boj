import itertools as i
print(sum(int(x)*int(y)for x,y in i.product(*input().split())))