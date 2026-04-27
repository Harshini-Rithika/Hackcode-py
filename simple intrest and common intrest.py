#simple intrest and common intrest
p=int(input("enter the value of p:"))
t=int(input("enter the value of t:"))
r=int(input("enter the value of r:"))
SI=(p*t*r)/100
CI=p*(1+r/100)**t-p
print("simple interest is",SI,"and compound intrest is",CI)