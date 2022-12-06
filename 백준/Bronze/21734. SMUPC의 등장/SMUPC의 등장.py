text = [i for i in input()]
nums = [str(ord(j)) for j in text]
count = [sum(int(i) for i in j) for j in nums]
for a,b in zip(count, text):
    print(a*b)