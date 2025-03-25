lamd = int(input())
color = "can not see"
if lamd <= 780:
    if lamd >= 620:
        color = "Red"
    elif lamd >= 590:
        color = "Orange"
    elif lamd >= 570:
        color = "Yellow"
    elif lamd >= 495:
        color = "Green"
    elif lamd >= 450:
        color = "Blue"
    elif lamd >= 425:
        color = "Indigo"
    elif lamd >= 380:
        color = "Violet"

print(color)