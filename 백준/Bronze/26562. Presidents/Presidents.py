import sys
p_name = ['Franklin', 'Grant', 'Jackson', 'Hamilton', 'Lincoln', 'Washington']
p_value = [100, 50, 20, 10, 5, 1]
p_dict = dict(zip(p_name, p_value))

N = int(sys.stdin.readline().strip())
for i in range(N):
    total_value = 0
    p_list = sys.stdin.readline().strip().split()
    for p in p_list: total_value += p_dict.get(p)
    print(f"${total_value}")