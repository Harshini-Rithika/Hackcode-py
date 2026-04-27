#LCM of the two number
import math
a=int(input("enter A:"))
b=int(input("enert B:"))
lcm=(a*b)//math.gcd(a,b)
print("LCM= ",lcm)