l=lambda:sum(map(ord,input()))
print(["YES","NO"][l()-l()&1])