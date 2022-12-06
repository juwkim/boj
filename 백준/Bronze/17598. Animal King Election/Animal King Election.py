import sys
print('Lion' if sys.stdin.read().count('L') > 4 else 'Tiger')