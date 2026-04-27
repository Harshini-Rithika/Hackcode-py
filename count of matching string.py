
def match(words):
   count=0
   for word in words:
      if len(word)>=2 and word[0]==word[-1]:
        count+=1
      return count
word_list=input("enter words seperated by space:").split()
result=match(word_list)
print("count of matching strings:",result)