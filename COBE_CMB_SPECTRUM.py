import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#data loaded
frequency=np.loadtxt('data.txt',usecols=0)
cmb_flux=np.loadtxt('data.txt',usecols=1)

#constants
c=2.99792458e8
T=2.725
h=6.626e-34
c=3.e8
k=1.38e-23
"""
Changing cm^(-1)  to Hz
"""
frequency=(frequency*c*100)

def BB(v):
 return (2.*h*(v**3)/(c**2))*(1./(np.exp(h*v/(k*T))-1.))
	

print(BB(frequency))
plt.plot(frequency,BB(frequency),'k-',label='BB-spectrum')
plt.plot(frequency,cmb_flux*10**-20,'r.',label='CMB-data')
plt.xlabel('frequency(Hz)')
plt.ylabel('flux(SI)')
plt.legend()
plt.savefig('spectrum.png',dpi=500)
plt.show()

#finding maximum
BBspec=BB(frequency)
print()
#frequency_max=frequency[BBspec.index(np.max(BBspec))]
peaks,_= find_peaks(BBspec)
print(frequency[peaks])
"""
1.635e+11 is the peak frequency and it lies in microwave region.

"""
