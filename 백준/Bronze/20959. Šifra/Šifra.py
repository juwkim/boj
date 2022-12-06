import re
print(len(set(re.sub('[\D]',' ',input()).split())))