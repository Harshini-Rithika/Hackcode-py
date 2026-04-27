# check the string
def check_string(s):
   if len(s)>=2:
      if s[0]== s[-1]:
       return True
      return False

a="level"
result=check_string(a)
if result:
   print("yes the given string satisfied")
else:
   print("no the given string does not satisfy")