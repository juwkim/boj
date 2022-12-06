import itertools as i
print(len({*map(sum,i.combinations_with_replacement((1,5,10,50),int(input())))}))