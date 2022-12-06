from functools import reduce
g = lambda: sorted(reduce(lambda x, y: x.update({y:x.get(y, 0)+1}) or x, input(), {}).values())
print(['NO', 'YES'][g() == g()])