from GWS import UnitGWS
import numpy as np
import matplotlib.pyplot as plt

# Single rotating source properties
d = 10                               # Distance to the source in kpc
e = 1                                # Equatorial ellipticity in (e/10^-6) units
I3 = 1                               # I_{zz} in (I_{zz}/I0) units
eta = 0                              # Inclination angle of the source in degrees
f = np.linspace(0.1, 1500, 100)      # Frequency array  

# Create instances of the class
src = UnitGWS(d, e, I3, eta, f)

# Calculate the radiated power for the single rotating source
power_radiated = src.GWpower()

# Calculate the gravitational wave strain for the single rotating source
h0 = src.optimalStrain()
hp, hx = src.strain(1)

# Plots
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(f, h0, label = 'Optimal Pointing')
ax1.scatter(f, hp, label = '+ Pol')
ax1.scatter(f, hx, label = 'x Pol')  
ax2.plot(f, power_radiated, label = 'Power emitted')
ax2.set(xlabel='frequency (in Hz)')
ax1.set_ylabel('Gravitational Wave Strain')
ax2.set_ylabel('Power Emitted')
ax1.legend()
ax2.legend()
plt.show()