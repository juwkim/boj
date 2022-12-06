import sys
for line in sys.stdin:
    print('yes' if 'problem' in line.lower() else 'no')