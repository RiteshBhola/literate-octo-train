S='mumbai' 
sum=0
t=0
unicod=list()
for element in S:
  t=ord(element)
  print(element,t)
  sum=sum+t
  unicod.append(t)

print("Sum of unicode of letters of mumbai:",sum)
print("The Required list is:")
print(unicod)
  
