temp=str(input("enetr the temperature:")).lower()
hum=str(input("enter the humidity:")).lower()
if temp=="warm" and hum=="dry":
   print("play basket ball")
elif temp=="warm" and hum=="humid":
   print("play tennis")
elif temp=="cold" and hum=="humid":
   print("swim")
elif temp=="cold" and hum=="dry":
   print("play cricket")
else:
   print("invalid input")