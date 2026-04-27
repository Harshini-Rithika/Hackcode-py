num=int(input("enter any number:"))
for i in range (2,(num//2+1)):
   if num%i==0:
      print("the number is not prime")

   else:
      print("prime number")