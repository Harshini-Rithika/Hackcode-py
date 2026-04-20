import itertools
A_input = input().strip().split()
A = [int(x) for x in A_input]
B_input = input().strip().split()
B = [int(x) for x in B_input]
cartesian_product = itertools.product(A, B)
product_list = list(cartesian_product)
print(*(f"({x}, {y})" for x, y in product_list))