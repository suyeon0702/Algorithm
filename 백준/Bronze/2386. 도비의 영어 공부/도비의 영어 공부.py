import sys
while 1:
    str_list = sys.stdin.readline().strip().split()
    alp = str_list[0]
    if alp == "#":
        break
    sample_str = ' '.join(str_list[1:])
    count = sample_str.lower().count(alp)
    print(f"{alp} {count}")