def solution(intStrs, k, s, l):
    answer = [int(new_str) for new_str in [Strs[s:s+l] for Strs in intStrs] if int(new_str) > k]
    return answer