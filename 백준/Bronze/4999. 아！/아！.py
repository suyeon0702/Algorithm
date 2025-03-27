import sys
a, b = sys.stdin.read().strip().split()
if b in a:
    print("go")
else:
    print("no")