def solution(age):
    alp_dict = dict(zip('0123456789', 'abcdefghij'))
    answer = ''
    for num in str(age):
        answer += alp_dict.get(num)
    
    return answer