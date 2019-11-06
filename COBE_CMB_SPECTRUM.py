import numpy as np
import matplotlib.pyplot as plt

#data loaded
frequency=np.loadtxt('data.txt',usecols=0)
cmb_flux=np.loadtxt('data.txt',usecols=1)

#constants
c=3.e8
T=2.725
h=6.626e-34
c=3.e8
k=1.38e-23

frequency=(frequency*c*100)

def BB(v):
 return (2.*h*(v**3)/(c**2))*(1./(np.exp(h*v/(k*T))-1.))
	

print(BB(frequency))
plt.plot(frequency,cmb_flux*10**-20,'r.',label='CMB-data')
plt.plot(frequency,BB(frequency),'k-',label='BB-spectrum')
plt.xlabel('frequency(Hz)')
plt.ylabel('flux(SI)')
plt.legend()
#plt.savefig('abc.png',dpi=500)
plt.show()

