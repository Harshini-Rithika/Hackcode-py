n=int(input("enter any number:"))
f=0
s=1
print("fibonacci series")
for i in range(0,n):
   print(f)
   next=f+s
   f=s
   s=next