a=str(input("enter any string"))
count1=0
count2=0
for i in a:
   if (i.isdigit()):
      count1+=1
      count2+=1
print("number of digits is:",count1)
print("number of character is:",count2)
spacecount=a.count(" ")
print(spacecount)