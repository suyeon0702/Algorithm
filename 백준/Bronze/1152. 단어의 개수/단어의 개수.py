import sys

sample_string = sys.stdin.readline().lstrip().rstrip()
if sample_string == '':
    print(0)
else:
    print(sample_string.count(' ')+1)