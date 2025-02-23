def solution(binomial):
    bin_list = binomial.split()
    op = bin_list[1]
    a, b, = int(bin_list[0]), int(bin_list[-1])
    if op == "+": return a+b
    elif op == "-": return a-b
    elif op == "*": return a*b