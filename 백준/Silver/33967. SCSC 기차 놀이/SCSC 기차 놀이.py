from itertools import pairwise

print(int(input()) - 1 + sum((l in "22 55") - (l == "][") for l in map("".join, pairwise(input()))))