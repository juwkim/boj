word = input().encode("UTF-8")
order = (word[0] - 234) * 64**2 + (word[1] - 176) * 64 + word[2] - 127
print(order)