def colours():
   colours=['blue','black','red','pink','green']
   l=len(colours)
   return l
def maxmin(lis):
   return min(lis),max(lis)
def sum_avg():
   s=sum(lis)
   avg=sum(lis)/len(lis)
   return s,avg
print("size of the list colours:",colours())
lis=[10,20,30,40,50]
mini,maxi=maxmin(lis)
print("minimum:",mini,"maximum:",maxi)
total,avg=sum_avg()
print("total:",total,"average:",avg)