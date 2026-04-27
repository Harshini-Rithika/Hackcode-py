def count_even_odd(numbers):
   odd_count=0
   even_count=0
   for number in numbers:
      if number%2==0:
       even_count+=1
      else:
       odd_count+=1
   return odd_count,even_count

#main
num=[1,2,3,4,45,11,28,8]
odd,even=count_even_odd(num)
print("odd numbers:",odd)
print("even numbers:",even)