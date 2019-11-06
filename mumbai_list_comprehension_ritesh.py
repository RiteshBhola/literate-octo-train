S='mumbai' 

d=[(i,ord(i)) for i in S]
print(d)

unicod=[ ord(i) for i in S ]
total=sum(unicod)

print("Sum of unicode of letters of mumbai:",total)
print("The Required list is:")
print(unicod)


