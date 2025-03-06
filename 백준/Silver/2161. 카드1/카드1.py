N = int(input())
card_list = [i for i in range(1, N+1)]
trash_can = []
while 1:
    if len(card_list) == 1:
        trash_can.append(str(card_list.pop()))
        break
    card = card_list.pop(0)
    trash_can.append(str(card))
    second_card = card_list.pop(0)
    card_list.append(second_card)

print(' '.join(trash_can))