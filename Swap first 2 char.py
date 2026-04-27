a=str(input("enter 1st string:"))
b=str(input("enter 2md string:"))
print("before swap:",a," ",b)
a1=b[:2]+a[2:]
b1=a[:2]+b[2:]
print("after swap:",a1," ",b1)