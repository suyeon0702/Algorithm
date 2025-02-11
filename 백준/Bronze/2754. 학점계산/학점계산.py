import sys

grade = sys.stdin.readline().strip()
score = -1
if "A" in grade:
    if "+" in grade: score = 4.3
    elif "0" in grade: score = 4.0
    elif "-" in grade: score = 3.7
elif "B" in grade:
    if "+" in grade: score = 3.3
    elif "0" in grade: score = 3.0
    elif "-" in grade: score = 2.7
elif "C" in grade:
    if "+" in grade: score = 2.3
    elif "0" in grade: score = 2.0
    elif "-" in grade: score = 1.7
elif "D" in grade:
    if "+" in grade: score = 1.3
    elif "0" in grade: score = 1.0
    elif "-" in grade: score = 0.7
elif grade == "F": score = 0.0

print(score)