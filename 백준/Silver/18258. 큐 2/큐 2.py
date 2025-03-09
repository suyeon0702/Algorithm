import sys
N = int(sys.stdin.readline().strip())
head, rear = 0, -1
q = []
for i in range(N):
    cmd = sys.stdin.readline().strip().split()
    order = cmd[0]

    if order == "push":
        new_num = int(cmd[1])
        q.append(new_num)
        rear += 1

    elif order == "pop":
        if head <= rear:
            pop_num = q[head]
            head += 1
            print(pop_num)
        else:
            print(-1)

    elif order == "size":
        length = rear-head+1
        print(length)

    elif order == "empty":
        length = rear-head+1
        if length == 0:
            print(1)
        else:
            print(0)

    elif order == "front":
        if head <= rear:
            head_num = q[head]
            print(head_num)
        else:
            print(-1)
        
    elif order == "back":
        if head <= rear:
            rear_num = q[rear]
            print(rear_num)
        else:
            print(-1)
        