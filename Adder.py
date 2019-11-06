
def adder(a,b):
 return(a+b)

def adder(*items):
 
 i=1
 while i< len(items):
  sum=sum+items[i]
  i=i+1
 return(sum)

def adder2(good=1,bad=2,ugly=3):
 return(good+bad+ugly)
 
def adder3(**kargs):
 for key in kargs.keys():
  value=kargs[key]
  print(value)
 return("Function over")
 


print(adder3(ugly=1,good=5,panda="black",complexd=3+4j))
