a=str(input("enter any string:"))
l=0
u=0
for i in a:
   if(i.islower()):
      l+=1
else:
   u+=1
print("lowercase=",l)
print("uppercase=",u)