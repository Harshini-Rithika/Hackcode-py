from collections import Counter
num_shoes = int(input())
shoes = Counter(map(int, input().split()))
num_customers = int(input())

total_money = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        total_money += price
        shoes[size] -= 1 
        
print(total_money)
