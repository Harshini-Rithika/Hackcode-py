def remove_duplicate(n):
   u=[]
   for i in n:
      if i not in u:
       u.append(i)
   return u
num=[10,25,10,47,25,3]
print("unique number:",remove_duplicate(num))