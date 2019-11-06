"""

FIbonacci program: This program prints first n fibonacci numbersG
02/09/2019
Ritesh Kr, Bhola

"""

def fibonacci(k):
	f0=0
	f1=1
	print(f0)
	for i in range(1,k):
		print(f1)
		temp=f0
		f0=f1
		f1=temp+f1


