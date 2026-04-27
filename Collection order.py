from collections import OrderedDict
item_sales = OrderedDict()
try:
    n = int(input())
except EOFError:
    n = 0
for _ in range(n):
    entry = input().split()
    price = int(entry[-1])
    item_name = " ".join(entry[:-1])
    if item_name in item_sales:
        item_sales[item_name] += price
    else:
        item_sales[item_name] = price
for item, total_price in item_sales.items():
    print(f"{item} {total_price}")

