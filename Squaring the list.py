def square_numbers(n):
   squares=[x**2 for x in range (1,n+1)]
   return squares

n=int(input("enter number:"))
squares_list=square_numbers(n)
print("list osf squares:",squares_list)