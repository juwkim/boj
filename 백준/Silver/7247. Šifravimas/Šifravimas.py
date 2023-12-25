key = "BI,GJNYTEO_RWSLHMDPZKFQUXCV.A"
val = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_,."
dic = {k: v for k, v in zip(key, val)}
ans = [dic[c] for c in input()]
print(*ans, sep="")