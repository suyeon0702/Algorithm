import sys
lines = sys.stdin.read().strip().split('\n')
red = int(lines[0])
green = int(lines[1])
blue = int(lines[2])

print(red*3+green*4+blue*5)