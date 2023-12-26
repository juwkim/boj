input()
a=0
for b in map(int, input().split()):a^=b
print(("Gleb\nMisha","Misha\nGleb")[a&1])