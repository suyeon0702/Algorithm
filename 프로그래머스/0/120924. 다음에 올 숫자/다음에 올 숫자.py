def solution(common):
    a1, a2, a3 = common[:3]
    
    if a2*2-a1 == a3:
        d = a2-a1
        an = common[-1]+d
    elif a2**2/a1 == a3:
        r = a2/a1
        an = common[-1]*r
    else:
        an = -1
        
    return an