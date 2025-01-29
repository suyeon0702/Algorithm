burger1 = int(input())
burger2 = int(input())
burger3 = int(input())
bv1 = int(input())
bv2 = int(input())

cheapest_set = min((burger1, burger2, burger3)) + min(bv1, bv2) - 50
print(cheapest_set)