def solution(my_string):
    answer = ''
    for alp in my_string:
        if alp < 'a':
            answer += alp.lower()
        else:
            answer += alp.upper()
    return answer