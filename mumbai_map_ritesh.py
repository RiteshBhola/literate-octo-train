S='mumbai' 
d=list(map(lambda x: (x,ord(x)),S))
print(d,"\n")

unicod=list(map(lambda x: ord(x),S))
total=sum(unicod)

print("Sum of unicode of letters of mumbai:",total,"\n")
print("The Required list is:")
print(unicod,"\n")
d=list(map(lambda x: (x,ord(x)),S))
print(d)
