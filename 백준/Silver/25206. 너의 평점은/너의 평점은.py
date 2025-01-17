grade_dict = {
    "A+" : 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}

sum_of_score = 0
sum_of_class = 0

for i in range(20):
    class_name, class_value, class_score = input().split(' ')
    class_value = float(class_value)
    if class_score != "P":
        class_score = grade_dict.get(class_score)
        sum_of_score += class_value * class_score
        sum_of_class += class_value

result_score = sum_of_score / sum_of_class

print(result_score)