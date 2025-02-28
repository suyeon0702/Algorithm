def solution(my_string, indices):
    new_string = ""
    for i in range(len(my_string)):
        if i in indices:
            pass
        else:
            new_string += my_string[i]
    return new_string