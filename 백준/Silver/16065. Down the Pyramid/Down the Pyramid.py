l,r=0,1e9
for a in map(int,[*open(0)][1].split()):l,r=max(0,a-r),a-l
print(max(0,r-l+1))